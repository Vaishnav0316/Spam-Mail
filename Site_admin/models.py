from django.db import models
from user.models import *
class Admin_tb(models.Model):
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class hobbyname_tb(models.Model):
    Hobbyname=models.CharField(max_length=20)
class hobbyfactor_tb(models.Model):
    Factorname=models.CharField(max_length=20)
    Hobby_id=models.ForeignKey(hobbyname_tb,on_delete=models.CASCADE)
class season_tb(models.Model):
    Season=models.CharField(max_length=20)
class seasonfactor_tb(models.Model):
    Factorname=models.CharField(max_length=20)
    Season_id=models.ForeignKey(season_tb,on_delete=models.CASCADE)
class seasoncountry_tb(models.Model):
    Seasonid=models.ForeignKey(season_tb,on_delete=models.CASCADE)
    SeasonFactorid=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
    Countryid=models.ForeignKey('user.country_tb',on_delete=models.CASCADE)
    Stateid=models.ForeignKey('user.state_tb',on_delete=models.CASCADE)
    Month=models.IntegerField()
class agefactor_tb(models.Model):
    MinimumAge=models.IntegerField()
    MaximumAge=models.IntegerField()
    Factorname=models.CharField(max_length=20)
    
