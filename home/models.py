from django.db import models

# Create your models here.
class contact(models.Model):
    
    email=models.CharField( max_length=122)
    password=models.CharField( max_length=12)
   
    def __str__(self):
        return self.email

class product(models.Model):
    pid=models.CharField( max_length=122)
    name=models.CharField( max_length=122)
    price=models.CharField( max_length=122)
    image=models.TextField()
    desc1=models.TextField()
    desc2=models.TextField()
    desc3=models.TextField()
    desc4=models.TextField()
    
    def __str__(self):
        return self.name



class dilivary(models.Model):
    pid=models.CharField( max_length=122)
    email=models.CharField( max_length=122)
    address=models.CharField( max_length=122)
    quantity=models.CharField( max_length=122)
    def __str__(self):
        return self.email


class card(models.Model):
    pid=models.CharField( max_length=122)
    email=models.CharField( max_length=122)
    address=models.CharField( max_length=122)
   
    image=models.TextField()
    price=models.CharField( max_length=122)
    disc1=models.TextField()
    disc2=models.TextField()

    def __str__(self):
        return self.email