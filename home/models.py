from django.core.validators import RegexValidator
from django.db import models

class idearegister(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    SEX = (
        (MALE, "Male"),
        (FEMALE, "Female"))

    firstName=models.CharField(max_length=20,)
    lastName=models.CharField(max_length=20,blank=False)
    sex = models.CharField(max_length=1, choices=SEX,verbose_name='Gender      ',blank=False)
   # phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$',
    #                             message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")
    phoneNumber = models.CharField(max_length=10, blank=True)  # validators should be a list
    mailId=models.EmailField(max_length=50,blank=False)
    ideaTitle=models.CharField(max_length=50,blank=False)
    idea=models.TextField(max_length=100,blank=False,verbose_name='Short Description of Idea(in 30-50 words)')
    headOfIdea=models.IntegerField(default=0)
    accessToIdea=models.IntegerField(default=0)
    ideaFile=models.FileField(upload_to='uploads/')
    checked=models.IntegerField(default=0) #we will check and then put up the idea on the main page

    def __str__(self):
        return self.ideaTitle+"  "+self.firstName+"  "+self.lastName+" "+self.mailId

class addques(models.Model):
        name = models.CharField(max_length=15)
        question = models.TextField(max_length=100)
        timetaken = models.IntegerField(default=0)
        idForum = models.IntegerField(default=-999999)

        def __str__(self):
            return self.name + "  " + self.question
