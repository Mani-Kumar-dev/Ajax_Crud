from django.db import models


class Employee(models.Model):
    GENDER_CHOICES = [
         ('M','Male'),
         ('F','Female'),
         ('O','Other'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    phoneNo = models.CharField(max_length=15)
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    companyName = models.CharField(max_length=100)
    fromDate = models.CharField(max_length=10)
    toDate = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    qualificationName = models.CharField(max_length=100)
    percentage = models.FloatField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo=models.ImageField(upload_to="images",null=True,blank=True)
    def __str__(self):
        return self.name
