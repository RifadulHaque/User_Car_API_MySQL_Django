from django.shortcuts import render
from django.http import JsonResponse
from userApp.models import User

# Create your views here.
def userView(request):
    #static user object which is returned as a JSON
    #dictionary in Python is like hashmap of Java
    usr = {
        'id':1,
        'name':'Tester1',
        'age': 24,
        'profession':'Developer',
        'sal':1000000,
        'email':'tester1@gmail.com'
    }

    data = User.objects.all();#fetch all the records in the database
    response = {'user':list(data.values('name','sal', 'age', 'profession', 'email'))}


    #return JsonResponse(usr)
    return JsonResponse(response)