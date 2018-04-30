from django.db import models

# Create your models here.

class officialpoststbl(models.Model):
    username = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=10000)
    messagedate = models.DateField("Date", auto_now_add=True)

    def __str__(self):
        return self.name

class eventspoststbl(models.Model):
    username = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=10000)
    messagedate = models.DateField("Date", auto_now_add=True)

    def __str__(self):
        return self.name


class buysellpoststbl(models.Model):
    username = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=10000)
    messagedate = models.DateField("Date", auto_now_add=True)

    def __str__(self):
        return self.name


class sportspoststbl(models.Model):
    username = models.CharField(max_length=100)
    emailid = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    message = models.CharField(max_length=10000)
    messagedate = models.DateField("Date", auto_now_add=True)

    def __str__(self):
        return self.name
