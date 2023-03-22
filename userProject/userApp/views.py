from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def userView(request):
    user = {
        'id':1,
        'name':'Tester1',
        'age': 24,
        'prefession':'Developer',
        'sal':1000000,
        'email':'tester1@gmail.com'
    }

    return JsonResponse(user)