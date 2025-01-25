from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Order

@shared_task
def send_order_email(order_id):
    """
    Send an email notification to the supplier when a new order is created.
    """
    try:
        order = Order.objects.get(id=order_id)

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
        subject = f"Replenishment Order for {order.product.name}"
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

        return f"Email sent to {order.supplier.email}"
    except Order.DoesNotExist:
        return "Order not found"