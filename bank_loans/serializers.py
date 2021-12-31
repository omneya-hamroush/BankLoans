from rest_framework import serializers
from bank_loans import models


class FundSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fund
        fields = "__all__"



class LoanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Loan
        fields = "__all__"


class FundApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FundApplication
        fields = "__all__"


class LoanApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LoanApplication
        fields = "__all__"

