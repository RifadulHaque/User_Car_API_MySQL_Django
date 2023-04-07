"""userProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from userApp import views
from rest_framework import routers
from userApp.views import CarViewSet, UserViewSet #used interms of Nested Serialization using viewSets


#used for nested Serialization viewSets
router = routers.DefaultRouter()
router.register('user',UserViewSet)
router.register('car',CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]


#used for mixins, generics etc
"""
urlpatterns = [
    # path('users/',views.user_list),
    # path('users/<int:pk>',views.user_details)
    path('user/',views.UserList.as_view()), #used for generics
    path('user/<int:pk>',views.UserDetails.as_view()), #used for generics
    path('car/',views.CarList.as_view()), #used for generics
    path('car/<int:pk>',views.CarDetails.as_view()) #used for generics
]
"""