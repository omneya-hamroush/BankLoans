from rest_framework import serializers
from userApp import models






class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = "__all__"
        
        extra_kwargs = {
            'password': {'write_only': True}
        }
