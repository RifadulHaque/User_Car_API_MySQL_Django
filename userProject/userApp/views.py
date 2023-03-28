from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def userView(request):
    #static user object which is returned as a JSON
    #dictionary in Python is like hashmap of Java
    user = {
        'id':1,
        'name':'Tester1',
        'age': 24,
        'prefession':'Developer',
        'sal':1000000,
        'email':'tester1@gmail.com'
    }

    return JsonResponse(user)