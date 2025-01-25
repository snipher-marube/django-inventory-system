from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Supplier(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=15, unique=True, db_index=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=255, unique=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    threshold = models.PositiveIntegerField(default=10)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['name']

    def needs_reorder(self):
        return self.quantity < self.threshold
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders', db_index=True)
    quantity = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='orders', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order for {self.product.name} from {self.supplier.name}"
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural  = 'Orders'
        ordering = ['-created_at'] # order by most recent

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', db_index=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
        ordering = ['-created_at']

