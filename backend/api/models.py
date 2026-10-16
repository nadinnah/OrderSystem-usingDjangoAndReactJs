from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


# Create your models here.
class Product(models.Model):
    class Category(models.TextChoices):
        CAKES="cakes","Cakes"
        CUPCAKE="cupcakes","Cupcakes"
        COOKIES="cookies","Cookies"
        BROWNIES_BARS="brownies_bars","Brownies & Bars"
        PASTRIES="pastries","Pastries"
        BREAD="bread","Bread"
        PIES_TARTS="pies_tarts","Pies & Tarts"
        OTHER="other","Other"
        
    name= models.CharField(max_length=100)
    slug= models.SlugField(unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(blank=True, validators=[
        FileExtensionValidator(["jpg", "jpeg", "png", "webp"])
    ])
    category=models.CharField(max_length=20, choices=Category.choices, default=Category.CAKES)
    is_available= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING= "pending", "Pending"
        CONFIRMED= "confirmed", "Confirmed"
        READY="ready","Ready"
        PICKED_UP="picked_up", "Picked up"
        CANCELLED="cancelled", "Cancelled"

    customer=models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_date=models.DateField()
    status=models.CharField(choices=Status.choices, default=Status.PENDING, max_length=20)
    notes=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    
    