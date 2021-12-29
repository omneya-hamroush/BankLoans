from django.urls import path, include

from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from bank_loans import views


router = DefaultRouter()

urlpatterns = [
    url(r'^getfunds', views.GetFunds.as_view()),
    url(r'^getp', views.GetP.as_view()),
    url(r'^amortization', views.FundAmort.as_view()),
]
