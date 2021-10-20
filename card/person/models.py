from django.db import models


class Person(models.Model):
    card_nunber = models.CharField(max_length=9, unique=True)
    first_name = models.CharField(max_length=48)
    last_name = models.CharField(max_length=48)
    photo = models.ImageField(upload_to='photo')
    Citizen = models.CharField(max_length=24)
    class SexType(models.TextChoices):
        M = 'M', 'Male'
        F = 'F', 'Female'
    sex = models.CharField(
        max_length=1,
        choices=SexType.choices,
    )
    personal_number = models.SmallIntegerField(unique=True)
    Birth_date = models.DateField()
    expiry_date = models.DateField()
    Birth_place = models.CharField(max_length=120)
    issue_date = models.DateField()
    issuing_authority = models.CharField(max_length=256)
