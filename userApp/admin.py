from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from userApp import models

admin.site.register(models.User)
# @admin.register(models.User)
# class UserAdmin(BaseUserAdmin):
#     list_display = [
#         "id",
#         "email",
#         "first_name",
#         "last_name",
#         "is_loan_provider",
#         "is_loan_customer",
#         "is_bank_personnel"
#     ]
#     ordering = ("-id",)
