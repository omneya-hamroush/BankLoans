from django.urls import path, include

from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from bank_loans import views


router = DefaultRouter()
router.register('fund', views.FundViewSet, basename= 'fund')
router.register('loan', views.LoanViewSet, basename= 'loan')


urlpatterns = [
    url(r'^getfunds', views.GetFunds.as_view()),
    url(r'^getloans', views.GetLoans.as_view()),
    url(r'^amortization', views.FundAmort.as_view()),
    url(r'^loanterms', views.GetLoanTerms.as_view()),
    url(r'^addfund', views.AddFund.as_view()),
]
