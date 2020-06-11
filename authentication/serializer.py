from rest_framework import serializers
from authentication.models import ExtentedUser
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = '__all__'

class ExtendedUserSerializer(serializers.ModelSerializer):
    user_data = UserSerializer()
    class Meta:
        model = ExtentedUser

        fields ='__all__'