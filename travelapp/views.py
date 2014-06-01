from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group

from travelapp.serializers import UsersSerializer,GroupsSerializer
from travelapp.models import Users, Groups
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


@api_view(('GET',))
def api_root(request, year):
    user = Users.objects.get(pk=1)
    s = UsersSerializer(user)

    #return Response(s.data)
    return Response(
    {
        'year':year
    }
    )


class UsersList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    paginate_by = 2
    
class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer  
    
class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer     
    
class GroupsList(generics.ListAPIView):    
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    
class CreateUser(generics.CreateAPIView):
    #queryset = Users.objects.all()
    serializer_class = UsersSerializer

class CreateGroup(generics.CreateAPIView):
    #queryset = Users.objects.all()
    serializer_class = GroupsSerializer
    
    
    
