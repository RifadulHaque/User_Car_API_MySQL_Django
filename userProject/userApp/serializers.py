from rest_framework import serializers
from userApp.models import User,Car

class CarSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Car
        #fields =['car_name','brand','year','user']
        fields='__all__'

class UserSerialzier(serializers.ModelSerializer):
    # line below is used for nested serialization
    cars = CarSerialzier(read_only=True, many=True) #this line makes it a nested serializer
    class Meta:
        model = User
        #fields = ['name','age','profession','sal','email','cars']
        fields = '__all__'
