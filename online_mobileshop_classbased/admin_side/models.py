from django.db import models

# Create your models here.

class Brand(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)


    def __str__(self):
        return str(self.brand_name)


class Mobile(models.Model):
    mobile_name=models.CharField(max_length=120,unique=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    ram=models.CharField(max_length=150)
    storage=models.CharField(max_length=150)
    camera=models.CharField(max_length=150)
    os=models.CharField(max_length=120)
    price=models.IntegerField()
    images=models.ImageField(upload_to="images")


    def __str__(self):
        return self.mobile_name