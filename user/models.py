from django.db import models
from Site_admin.models import *
class country_tb(models.Model):
    Country=models.CharField(max_length=20)
class state_tb(models.Model):
    State=models.CharField(max_length=20)
    Country_id=models.ForeignKey(country_tb,on_delete=models.CASCADE)
class register_tb(models.Model):
    Name=models.CharField(max_length=20)
    Gender=models.CharField(max_length=20)
    DOB=models.CharField(max_length=20)
    Address=models.CharField(max_length=20)
    Countryid=models.ForeignKey(country_tb,on_delete=models.CASCADE)
    Stateid=models.ForeignKey(state_tb,on_delete=models.CASCADE)
    Phone=models.CharField(max_length=20)
    SecurityQuestion=models.CharField(max_length=20)
    Answer=models.CharField(max_length=20)
    Username=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
class hobby_tb(models.Model):
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Hobbyid=models.ForeignKey(hobbyname_tb,on_delete=models.CASCADE)
class message_tb(models.Model):
    Senderid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='Senderid')
    Subject=models.CharField(max_length=20)
    Message=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Receiverid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Status=models.CharField(max_length=20,default="Pending")
    FilterStatus=models.CharField(max_length=20,default="Pending")
class trash_tb(models.Model):
    Messageid=models.ForeignKey(message_tb,on_delete=models.CASCADE)
    Receiverid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
class Contact_tb(models.Model):
    Contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='Userid')
    Name=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Remarks=models.CharField(max_length=20)
class Blocklist_tb(models.Model):
    Contactid=models.ForeignKey(register_tb,on_delete=models.CASCADE,related_name='Contactid')
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Name=models.CharField(max_length=20)
    Date=models.CharField(max_length=20)
    Time=models.CharField(max_length=20)
    Remarks=models.CharField(max_length=20)
class Customerhobby_tb(models.Model):
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Hobbyid=models.ForeignKey(hobbyname_tb,on_delete=models.CASCADE)
    Factorid=models.ForeignKey(hobbyfactor_tb,on_delete=models.CASCADE)
class Customeragefactor_tb(models.Model):
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Factorid=models.ForeignKey(agefactor_tb,on_delete=models.CASCADE)
class CustomerSeasoncountry_tb(models.Model):
    Userid=models.ForeignKey(register_tb,on_delete=models.CASCADE)
    Factorid=models.ForeignKey(seasonfactor_tb,on_delete=models.CASCADE)
    

