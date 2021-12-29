from django.shortcuts import render
from bank_loans import models, serializers
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


class GetFunds(APIView):
    permission_classes = (permissions.ProviderPermission,)
    authentication_classes = (TokenAuthentication,)
    def get(self,request):
        query_params = self.request.query_params
        amount = self.request.query_params.get('amount')
        queryset = models.Fund.objects.all()
        queryset = queryset.filter(minimum__lte=amount, maximum__gte=amount)
        serializer = serializers.FundSerializer(queryset, many=True,context={'request':request})
        return Response({"data": serializer.data})


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






class FundAmort(APIView):
    permission_classes = (permissions.ProviderPermission,)
    authentication_classes = (TokenAuthentication,)
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
        # return Response({
        #    table
        # })


class GetP(APIView):
    def get(self,request):
        query_params = self.request.query_params
        fund_id = self.request.query_params.get('fund_id')

        fund = models.Fund.objects.get(id=fund_id)
        payment = fund.paymentValue
        return Response({payment})
        # serializer = serializers.FundSerializer(queryset, many=True,context={'request':request})
