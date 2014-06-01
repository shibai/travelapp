from django.db import models

# Create your models here.

class Users(models.Model):
    email = models.EmailField(max_length=75,unique = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    password = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    typeT = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    url = models.CharField(max_length=75)
    
    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)
        
      
class Groups(models.Model):
    name = models.CharField(max_length=30, unique = True)
    users = models.ForeignKey(Users, related_name = 'owenedGroups')
    members = models.ManyToManyField(Users)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    typeT = models.CharField(max_length=30)
    deleted = models.BooleanField(default = False)
    content = models.TextField()
    
    def __unicode__(self):
        return str(self.name)

class Trips(models.Model):
    name = models.CharField(max_length=30, unique = True)
    groups = models.ForeignKey(Groups, related_name = 'owenedTrips')
    members = models.ManyToManyField(Users)
    fromLoc = models.CharField(max_length=30)
    toLoc = models.CharField(max_length=30)
    typeT = models.CharField(max_length=30)
    deleted = models.BooleanField(default = False)
    content = models.TextField()
    
    def __unicode__(self):
        return str(self.owningGroup.name) + str(self.name)
    
    
    
    
    
    
    
    
    
    


        
        
        
        
        
        
        
        
        
        
        
        
        
        
