from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class book(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    Title = models.CharField(max_length=50)
    Book_image = models.ImageField(upload_to="BooksImages")
    Auth = models.CharField(max_length=20)
    Rating = models.IntegerField()
    Book = models.FileField(upload_to="books")

    
    def __str__(self):
        return self.Title