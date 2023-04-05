from rest_framework import serializers
from userApp.models import User

class UserSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','age','profession','sal','email']
