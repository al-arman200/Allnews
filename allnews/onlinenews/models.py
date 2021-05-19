from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Agency(models.Model):
    address_site    = models.CharField(max_length=50)
    name            = models.CharField(max_length=50)
    description     = models.TextField()
    def __str__(self):
        return self.name

class News(models.Model):
    agency      = models.ForeignKey('Agency' , on_delete=models.CASCADE)
    title       = models.CharField(max_length=150)
    link        = models.CharField(max_length=100)
    typenews    = models.CharField(max_length=1 , choices=[('f','فناوری'),('v','ورزشی'),('e','اقتصادی'),('s','سیاسی'),])
    pub_date    = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
