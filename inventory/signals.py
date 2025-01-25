from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
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
        # Send email notification to the supplier
        subject = f"Replenishment Order for {instance.name}"
        message = render_to_string('inventory/order_email.html', {'order': order})
        send_mail(subject, message, 'noreply@inventory.com', [instance.supplier.email])

        # Create a notification for the admin
        admin_users = User.objects.filter(is_staff=True)
        for user in admin_users:
            Notification.objects.create(
                user=user,
                message=f"New order created for {instance.name}"
            )