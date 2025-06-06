from rest_framework import serializers
from .models import Customer
from django.contrib.auth.models import User
import re

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def validate_mobile(self, value):
        if not re.match(r'^\+?\d{10,15}$', value):
            raise serializers.ValidationError("Invalid mobile number format.")
        return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

