from django.db import models


class Pizza(models.Model):
    """This class represent the Pizza model"""
    name = models.CharField(max_length=50)


class Customer(models.Model):
    """This class represent the Customer model"""
    name = models.CharField(max_length=50, unique=True)
    adress = models.TextField()


class Order(models.Model):
    """This class represent the Order model"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name='order_with_pizza')
    PIZZA_SIZE_CHOICES = (('50', '50cm'), ('30', '30cm'))
    pizza_size = models.CharField(max_length=2, choices=PIZZA_SIZE_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_order')
