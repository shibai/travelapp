from django.contrib.auth.models import User, Group
from rest_framework import serializers
from travelapp.models import Users,Groups,Trips


class UsersSerializer(serializers.HyperlinkedModelSerializer):
   # email = serializers.EmailField()
    owenedGroups = serializers.HyperlinkedRelatedField(many=True,view_name = 'groups-detail',read_only=True)
    class Meta:
        model = Users
        fields = ('id', 'email','owenedGroups','first_name','last_name','password','address', \
        'city','state','zipcode','country','typeT','phone','url')

class GroupsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(source='users',view_name = 'users-detail')
    class Meta:
        model = Groups
        fields = ('id', 'name','owner','members','city','state','country','typeT','deleted','content')
        
class TripsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(source='groups',view_name = 'groups-detail')
    class Meta:
        model = Trips
        fields = ('id', 'name','groups','members','fromLoc','toLoc','typeT','deleted','content')        
        
