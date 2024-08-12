from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class category(models.Model):
  category_name=models.CharField(max_length=100,unique=True)
  is_active=models.BooleanField(default=True)

  def __str__(self):
    return self.category_name

class product(models.Model):
  product_name=models.CharField(max_length=100)
  price=models.PositiveIntegerField()
  image=models.ImageField(upload_to="media/product")
  description=models.TextField(max_length=200)
  category=models.ForeignKey(category,on_delete=models.CASCADE)

  def __str__(self):
    return self.product_name

class cart(models.Model):
  product_name=models.ForeignKey(product,on_delete=models.CASCADE)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  quantity=models.PositiveIntegerField(default=1)
  options=(
    ("in-cart","in-cart"),
    ("canceiled","canceiled"),
    ("order-placed","order-placed"),
  )
  status=models.CharField(max_length=100,default="in-cart",choices=options)
  date=models.DateField(auto_now_add=True)

  def __str__(self):
    return self.product_name.product_name

class orders(models.Model):
  product_name=models.ForeignKey(cart,on_delete=models.CASCADE)
  address=models.TextField(max_length=200)
  phone=models.IntegerField()
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  options=(
    ("dispatched","dispatched"),
    ("canceiled","canceiled"),
    ("order-placed","order-placed"),
    ("delivered","delivered"),
  )
  status=models.CharField(max_length=100,default="f",choices=options)
  date=models.DateField(auto_now_add=True)
