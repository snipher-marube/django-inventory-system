from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Product, Order, Notification
from .tasks import send_order_email

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

        # Trigger the celery task to send the email
        send_order_email.delay(order.id)

        # create a notification for the admin
        admin_users = User.objects.filter(is_staff=True)
        for user in admin_users:
            Notification.objects.create(
                user=user,
                message=f"New order created for {instance.name}"
            )