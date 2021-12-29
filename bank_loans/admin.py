from django.contrib import admin

from bank_loans import models


admin.site.register(models.Loan)
admin.site.register(models.Fund)
