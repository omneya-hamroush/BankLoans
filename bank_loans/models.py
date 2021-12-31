from django.db import models
# from .utils import LoanMixin
# Create your models here.


class Loan(models.Model):
    amount = models.FloatField(null=True, blank=True)
    minimum = models.FloatField(null=True, blank=True)
    maximum = models.FloatField(null=True, blank=True)
    interest_rate = models.FloatField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)


class Fund(models.Model):
    amount = models.FloatField(null=True, blank=True)
    minimum = models.FloatField(null=True, blank=True)
    maximum = models.FloatField(null=True, blank=True)
    interest_rate = models.FloatField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    # validators=[
    #         MaxValueValidator(100),
    #         MinValueValidator(1)
    #     ]
