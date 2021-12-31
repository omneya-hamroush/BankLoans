from django.shortcuts import render
from bank_loans import models, serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from BankLoans import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from numpy_financial import pmt
# from django.utils import simplejson
import json
from django.http import HttpResponse
from rest_framework import status


# function to return all the data for the amortization table
def amortization(rate, amount, monthly_payment, term):
    monthly_rate = rate/12
    balance = amount
    print("vvvvvvvvvvv")
    print(balance)
    x = []
    i = 0
    while balance > 0:
        l = {}
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance = balance - principal
        l = {"Month":i+1, "Payment":monthly_payment, "Interest":interest, "principal":principal, "Balance":balance}
        x.append(l)
        i = i + 1
    return x

# to get all the funds that the amount is within
class GetFunds(APIView):
    # permission_classes = (permissions.ProviderPermission,)
    # authentication_classes = (TokenAuthentication,)
    def get(self,request):
        query_params = self.request.query_params
        amount = self.request.query_params.get('amount')
        queryset = models.Fund.objects.all()
        queryset = queryset.filter(minimum__lte=amount, maximum__gte=amount, amount=None)
        serializer = serializers.FundSerializer(queryset, many=True,context={'request':request})
        print(serializer.data)
        if serializer.data == []:
            return Response({"No matching funds"})
        else:

            return Response({"data": serializer.data})


# to return amortization table for the fund
class FundAmort(APIView):
    # permission_classes = (permissions.ProviderPermission,)
    # authentication_classes = (TokenAuthentication,)
    def get(self,request):
        query_params = self.request.query_params
        fund_id = self.request.query_params.get('fund_id')
        amount = self.request.query_params.get('amount')
        fund = models.Fund.objects.get(id=fund_id)
        print("cccccccccc")
        print(fund)
        print(type(int(amount)))
        print(type(fund.interest_rate))
        print(type(12))
        print("xxxxxxxxxxx")
        months = fund.duration * 12
        print(months)
        rate = (fund.interest_rate / 100)
        print(rate)
        amount = int(amount)
        payment = -(pmt(rate/12, months, amount))
        print(payment)
        table = amortization(rate, amount, payment, months)
        print(table)
        amort_table = json.dumps({"amortization_table" : table})
        return HttpResponse(amort_table, content_type ="application/json")


# returns all the available loans durations
class GetLoanTerms(APIView):
    authentication_classes = (TokenAuthentication,)
    def get(self,request):
        queryset = models.Loan.objects.all()
        x = []
        for i in queryset:
            x.append(i.duration)
        l = list( dict.fromkeys(x) )
        return Response(l)



class AddFund(APIView):
    def post(self,request):
        query_params = self.request.query_params
        fund_id = self.request.query_params.get('fund_id')
        fund = models.Fund.objects.get(id=fund_id)
        print(fund_id)
        print("ccccccccc")
        amount = self.request.query_params.get('amount')
        print("iiiiiiiiiiiiii")
        print(type(amount))
        print(amount)


        fund_data = {"amount":amount, "minimum":fund.minimum, "maximum":fund.maximum, "interest_rate": fund.interest_rate,
        "duration":fund.duration
        }
        loan, created = models.Fund.objects.update_or_create(
        **fund_data
        )
        serializer = serializers.FundSerializer(loan, context={'request':request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoanViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LoanSerializer
    queryset = models.Loan.objects.all()



class FundViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FundSerializer
    queryset = models.Fund.objects.all()
    # permission_classes = (permissions.ProviderPermission,)
    # authentication_classes = (TokenAuthentication,)

    # def create(self, request):
        # query_params = self.request.query_params
        # amount = int(self.request.query_params.get('amount'))
        # print(amount)
        # fund_id = self.request.query_params.get('fund_id')
        # fund = models.Fund.objects.get(id=fund_id)
        # print(fund_id)
        # print("ccccccccc")
        #
        # fund_data = {"amount":amount, "minimum":fund.minimum, "maximum":fund.maximum, "interest_rate": fund.interest_rate,
        # "duration":fund.duration
        # }
        # loan, created = models.Fund.objects.update_or_create(
        # **fund_data
        # )
        # serializer = self.get_serializer(loan)
        # return Response(serializer.data, status=status.HTTP_201_CREATED)
