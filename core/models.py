from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Job(models.Model):
    TYPE_CHOICES = (
        ('FullTime', 'FullTime'),
        ('Contract', 'Contract'),
        ('PartTime', 'PartTime'),
        ('Internship', 'Internship'),
    )

    LEVEL_CHOICES = (
        ('Intern', 'Intern'),
        ('Entry-level', 'Entry-level'),
        ('Mid-level', 'Mid-level'),
        ('Senior', 'Senior'),
        ('Manager', 'Manager'),
        ('Director', 'Manager'),
    )

    WORK_CHOICES = (
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid'),
        ('Onsite', 'Onsite'),
    )

    CURRENCY_CHOICES = (
        ('Naira', 'Naira'),
        ('USD', 'USD'),
        ('Euro', 'Euro'),
        ('Pounds', 'Pounds'),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, null=True)
    jobtype = models.CharField(max_length=200, choices=TYPE_CHOICES)
    level = models.CharField(max_length=200, choices=LEVEL_CHOICES)
    workplace = models.CharField(max_length=200, choices=WORK_CHOICES)
    description = models.TextField(null=True, blank=True)
    poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='job')
    currency = models.CharField(max_length=200, choices=CURRENCY_CHOICES, blank=True)
    minsalary = models.FloatField(null=True, blank=True)
    maxsalary = models.FloatField(null=True, blank=True)
    perks = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    link = models.CharField(max_length=1000, null=True)
    company = models.CharField(max_length=200, null=True)
    hearaboutus = models.CharField(max_length=200, null=True, blank=True)
    featured = models.BooleanField(default=False, null=True)

    def __str__(self):
        return  self.title