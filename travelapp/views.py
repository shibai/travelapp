from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group

from travelapp.serializers import UsersSerializer,GroupsSerializer, TripsSerializer
from travelapp.models import Users, Groups,Trips
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

    
class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer  
    
class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer     

class TripsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer     
 
class UsersList(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    paginate_by = 2

class GroupsList(generics.ListAPIView):    
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    paginate_by = 2

class TripsList(generics.ListAPIView):    
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    paginate_by = 2

class CreateUser(generics.CreateAPIView):
    #queryset = Users.objects.all()
    serializer_class = UsersSerializer

class CreateGroup(generics.CreateAPIView):
    #queryset = Users.objects.all()
    serializer_class = GroupsSerializer
    
class CreateTrip(generics.CreateAPIView):
    #queryset = Users.objects.all()
    serializer_class = TripsSerializer
       
    
