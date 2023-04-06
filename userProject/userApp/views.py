from django.shortcuts import render
from django.http import JsonResponse
from userApp.models import User,Car # added the User class from models
from userApp.serializers import UserSerialzier, CarSerialzier # import this for using the the UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view # used for function based views
from rest_framework.views import APIView #used for class based views
from django.http import Http404
from rest_framework import generics,mixins #used for mixins
from rest_framework import viewsets

"""
#Used for ViewSet, does the same work as Mixins and Generic Views
# With viewSets we can support both non-primary and primary views in one method
class UserViewSet(viewsets.ModelViewSet):
    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier    
"""

#Generic Views

#Non-Primary key based operations
class UserList(generics.ListCreateAPIView):
    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier

class CarList(generics.ListCreateAPIView):
    # it tells the mixin which model should be used
    queryset = Car.objects.all()
    #it tells which serializer class should be used
    serializer_class = CarSerialzier

#primary key based operations
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier    

class CarDetails(generics.RetrieveUpdateDestroyAPIView):
    # it tells the mixin which model should be used
    queryset = Car.objects.all()
    #it tells which serializer class should be used
    serializer_class = CarSerialzier   
    
# It is used for Mixins, It basically reduces the liens of code that is used for Class based and function based views
"""
class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class UserDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    # it tells the mixin which model should be used
    queryset = User.objects.all()
    #it tells which serializer class should be used
    serializer_class = UserSerialzier

    def get(self, requst, pk):
        return self.retrieve(requst, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)

"""


# It is used for class based View, works same as function based views

"""
class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerialzier(users, many = True)
        return Response(serializer.data)
    
    def post(self, request):
         #it converts the json data to post it in the DB
        serializer = UserSerialzier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
class UserDetails(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404
        
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerialzier(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerialzier(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""


# It is used for fucntion based views
"""
def userView(request):
    #static user object which is returned as a JSON
    #dictionary in Python is like hashmap of Java
    # usr = {
    #     'id':1,
    #     'name':'Tester1',
    #     'age': 24,
    #     'profession':'Developer',
    #     'sal':1000000,
    #     'email':'tester1@gmail.com'
    # }

    data = User.objects.all();#fetch all the records in the database
    # we return a dictionaly as it may contain multiple users
    # here user is the json key
    response = {'user':list(data.values('name','sal', 'age', 'profession', 'email'))}


    #return JsonResponse(usr)
    return JsonResponse(response)

@api_view(['GET','Post'])
def user_list(request):

    if request.method == 'GET':
        #users is the list of student objects
        users = User.objects.all() # it will give us all the user records
        #serializer contains the list of students which will be converted into json format from DB
        serializer = UserSerialzier(users, many = True )
        #the serializer will return the data in form of http resposne
        return Response(serializer.data)
    
    elif request.method == 'POST':
        #it converts the json data to post it in the DB
        serializer = UserSerialzier(data = request.data)
        if serializer.is_valid():
            #save the data in the DB
            serializer.save()
            #return the status and the data
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def user_details(request, pk):
    try:
        #we retrieve a single student using the primary key
        user = User.objects.get(pk=pk)
    except User.DoesNotExist :
        # if not founnd then show the status
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =  UserSerialzier(user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerialzier(user, data=request.data)
        # it checks if the data already exists or not
        if serializer.is_valid():
            #update the data
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""