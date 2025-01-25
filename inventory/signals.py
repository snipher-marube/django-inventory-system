from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives  # Use EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from .models import Product, Order, Notification

User = get_user_model()

@receiver(post_save, sender=Product)
def create_order_on_low_stock(sender, instance, **kwargs):
    """
    Automatically create an order if the product's quantity falls below the threshold.
    """
    if instance.needs_reorder():
        order = Order.objects.create(
            product=instance,
            quantity=instance.threshold - instance.quantity,
            supplier=instance.supplier
        )

        # Render the HTML email template
        html_message = render_to_string('inventory/order_email.html', {'order': order})

        # Create a plain text version of the email
        plain_text_message = f"""
        Replenishment Order Notification

        Dear {order.supplier.name},

        A new replenishment order has been created for the following product:

        Product Name: {order.product.name}
        Quantity to Order: {order.quantity}
        Order Created At: {order.created_at}

        Please process this order at your earliest convenience. If you have any questions, feel free to contact us.

        Thank you,
        {order.product.name} Inventory Management Team
        """

        # Send email notification to the supplier using EmailMultiAlternatives
        subject = f"Replenishment Order for {instance.name}"
        from_email = 'noreply@inventory.com'
        to_email = [order.supplier.email]

        email = EmailMultiAlternatives(
            subject=subject,
            body=plain_text_message,  # Plain text version
            from_email=from_email,
            to=to_email
        )
        email.attach_alternative(html_message, "text/html")  # Attach HTML version
        email.send()

        # Create a notification for the admin
        admin_users = User.objects.filter(is_staff=True)
        for user in admin_users:
            Notification.objects.create(
                user=user,
                message=f"New order created for {instance.name}"
            )