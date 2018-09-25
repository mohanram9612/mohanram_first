from django.db import models

# Create your models here.


class State(models.Model):
    state_name = models.CharField(max_length=15)


class District(models.Model):
    state = models.ForeignKey(State)
    district_name = models.CharField(max_length=20)


class Taluk(models.Model):
    district = models.ForeignKey(District)
    taluk_name = models.CharField(max_length=20)


class Pincode(models.Model):
    taluk = models.ForeignKey(Taluk)
    pincode = models.PositiveIntegerField()
