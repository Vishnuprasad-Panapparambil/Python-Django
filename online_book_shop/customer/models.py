from django.db import models

# Create your models here.

class Orders(models.Model):
    personname=models.CharField(max_length=120)
    address = models.CharField(max_length=200)
    pin = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    productid=models.IntegerField()
    user = models.CharField(max_length=20)

    choice={

        ('orderrecieved','orderrecieved'),
        ('dispached', 'dispached'),
        ('deliverd', 'deliverd'),
    }
    status=models.CharField(max_length=120,choices=choice,default='orderrecieved')
    active_status=models.IntegerField(default=1)

    def __str__(self):
        return self.personname



class BookCategory(models.Model):
    category_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.category_name

