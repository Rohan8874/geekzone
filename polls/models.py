from django.db import models

CATEGORY_CHOICES =(
    ('SP','Smart Phone'),
    ('LT','Leptop'),
    ('SW','Smart Watch'),
    ('EP','EarPods'),
    ('PB','Power Bank'),
    ('DP','Mini Digital Projector'),
    ('HC','Hardcover Case'),
    ('MF','Mini foldable Fan'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


# class Customer(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

# class Payment(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_date = models.DateTimeField(auto_now_add=True)

# class Delivery(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     address = models.CharField(max_length=200)
#     delivery_date = models.DateField()



# class Order(models.Model):
#     customer_name = models.CharField(max_length=255)
#     customer_email = models.EmailField()
#     customer_address = models.TextField()
#     products = models.ManyToManyField('Product', through='OrderItem')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default=ORDER_STATUS_PENDING)

#     # # def __str__(self):
#     #     return f'Order #{self.pk}'

# class OrderItem(models.Model):
#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f'{self.product} x {self.quantity}'

# class Cart(models.Model):
#     customer_name = models.CharField(max_length=255)
#     customer_email = models.EmailField()
#     products = models.ManyToManyField('Product', through='CartItem')
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f'Cart #{self.pk}'

# class CartItem(models.Model):
#     cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
#     product = models.ForeignKey('Product', on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f'{self.product} x {self.quantity}'
