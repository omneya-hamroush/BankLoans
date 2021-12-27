from django.db import models

# Create your models here.


class Loan(models.Model):
    amount = models.FloatField(null=True, blank=True)
    minimum = models.IntegerField(null=True, blank=True)
