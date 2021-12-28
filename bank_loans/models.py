from django.db import models

# Create your models here.


class Loan(models.Model):
    amount = models.FloatField(null=True, blank=True)
    minimum = models.FloatField(null=True, blank=True)
    maximum = models.FloatField(null=True, blank=True)
    interest_rate = models.FloatField(null=True, blank=True)
