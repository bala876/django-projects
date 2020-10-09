from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    dob = models.CharField(max_length=40)
    age = models.CharField(max_length=40)
    gender = models.CharField(max_length=40)
    mobilenumber = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    emailid = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    placedetails = models.CharField(max_length=40)
    pincode = models.CharField(max_length=40)
    def __str__(self):
        return self.firstname + " " + self.lastname  + " " + self.dob + " " + self.age + " " + self.gender + " " + self.mobilenumber + " " + self.address + " " + self.emailid + " " + self.password + " " + self.placedetails + " " + self.pincode  
