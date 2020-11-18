from django.db import models

# Create your models here.

class BookCategory(models.Model):
    category_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.category_name


class Book(models.Model):
    bookname=models.CharField(max_length=120)
    author=models.CharField(max_length=100)
    category=models.ForeignKey(BookCategory,on_delete=models.CASCADE)
    language=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)
    pages=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="images/")




    def __str__(self):
        return self.bookname
