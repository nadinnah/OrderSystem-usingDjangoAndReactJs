from django.db import models
from django.core.validators import FileExtensionValidator



# Create your models here.
class Product(models.Model):
    class Category(models.TextChoices):
        CAKE="cakes","Cakes"
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
    category=models.CharField(max_length=20, choices=Category.choices, default=Category.cakes)
    is_available= models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)