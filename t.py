
from travelapp.models import Users, Groups
from travelapp.serializers import UsersSerializer, GroupsSerializer

u = Users(email = '2@2',first_name = 'j',last_name = 's',password = '0', address = 'addr')
g = Groups(name = 'hha', users = u)
u = Users(email = '2@2',first_name = 'aa',last_name = 'bb',password = '0', address = 'addr')
