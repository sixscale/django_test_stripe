from django.db import models
from django.core import validators


class Product(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=70,
        verbose_name='Product Name'
    )

    description = models.TextField(
        max_length=800,
        verbose_name='Description'
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[
            validators.MinValueValidator(50),
            validators.MaxValueValidator(100000)
        ]
    )


class OrderDetail(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    product = models.ForeignKey(
        to=Product,
        verbose_name='Product',
        on_delete=models.PROTECT
    )

    amount = models.IntegerField(
        verbose_name='Amount'
    )

    stripe_payment_intent = models.CharField(
        max_length=200
    )

    has_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )


class Order(models.Model):
    items = models.ManyToManyField(Product)

    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2
    )

    stripe_payment_id = models.CharField(
        max_length=255
    )
