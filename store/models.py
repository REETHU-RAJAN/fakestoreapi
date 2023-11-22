from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

from datetime import date

class Category(models.Model):

    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    picture=models.ImageField(upload_to="images")
    price=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    # @property
    # def reviews(self):
    #     qs=self.reviews_set.all()
    #     return qs
    # @property
    # def avg_rating(self):
    #     ratings=self.reviews_set.all().values_list("rating",flat=True)
    #     return sum(ratings)/len(ratings) if ratings else 0
        
    def __str__(self):
        return self.name

class Carts(models.Model):
    products=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )

    status=models.CharField(max_length=200,choices=options,default="in-cart")
   


class Orders(models.Model):
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    options=(
      
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatced","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    orderd_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateField(null=True)
    address=models.CharField(max_length=200)


class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    



    


    






