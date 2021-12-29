from rest_framework import serializers
from bank_loans import models


class FundSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Fund
        fields = "__all__"

        
