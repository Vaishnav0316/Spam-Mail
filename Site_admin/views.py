from django.shortcuts import render,redirect
from Site_admin.models import *
from user.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"common/index.html")
def login(request):
    return render(request,"common/login.html")
def loginAction(request):
    username=request.POST['username']
    password=request.POST['password']
    admin=Admin_tb.objects.filter(Username=username,Password=password)
    user=register_tb.objects.filter(Username=username,Password=password)
    if(admin.count()>0):
        request.session['id']=admin[0].id
        return render(request,'admin/adminhome.html')
        messages.add_message(request,messages.INFO,"Login Succesfull")
    elif(user.count()>0):
        request.session['user_id']=user[0].id
        return render(request,'user/userhome.html')
        messages.add_message(request,messages.INFO,"Login Succesfull")
    else:
        messages.add_message(request,messages.INFO,"Invalid username or password")
        return render(request,"common/index.html")
def addhobby(request):
    return render(request,"admin/addhobby.html")
def SaveAction(request):
    hobbyname=request.POST['hobby']
    hobby=hobbyname_tb(Hobbyname=hobbyname)
    hobby.save()
    return render(request,'admin/adminhome.html')
    messages.add_message(request,messages.INFO,"Saved Succesfully")
def addhobbyfactor(request):
    hobby=hobbyname_tb.objects.all()
    return render(request,"admin/addhobbyfactor.html",{'ho':hobby})
def saveAction(request):
    factorname=request.POST['hobbyfactor']
    hid=request.POST['hobby']
    hobbyfactor=hobbyfactor_tb(Factorname=factorname,Hobby_id_id=hid)
    hobbyfactor.save()
    messages.add_message(request,messages.INFO,"Saved Succesfully")
    return render(request,'admin/adminhome.html')
def addseason(request):
    return render(request,"admin/addseason.html")
def SaveAction_season(request):
    seasonname=request.POST['season']
    season=season_tb(Season=seasonname)
    season.save()
    messages.add_message(request,messages.INFO,"Saved Succesfully")
    return render(request,'admin/adminhome.html')
def addseasonfactor(request):
    season=season_tb.objects.all()
    return render(request,"admin/addseasonfactor.html",{'se':season})
def saveAction_seasonfactor(request):
    factorname=request.POST['seasonfactor']
    sid=request.POST['season']
    seasonfactor=seasonfactor_tb(Factorname=factorname,Season_id_id=sid)
    seasonfactor.save()
    messages.add_message(request,messages.INFO,"Saved Succesfully")
    return render(request,'admin/adminhome.html')
def addseasoncountry(request):
    season=season_tb.objects.all()
    country=country_tb.objects.all()
    return render(request,"admin/addseasoncountry.html",{'se':season,'co':country})
def getseasonfactor(request):
    sid=request.GET['s']
    factor=seasonfactor_tb.objects.filter(Season_id_id=sid)
    return render(request,'admin/getfactor.html',{'f':factor})
def getstate_SC(request):
    countryid=request.GET['co']
    state=state_tb.objects.filter(Country_id_id=countryid)
    return render(request,'admin/getstate.html',{'st':state})
def addAction_SC(request):
    season=request.POST['season']
    factor=request.POST['factor']
    country=request.POST['country']
    state=request.POST['state']
    month=request.POST['month']
    user=seasoncountry_tb(Seasonid_id=season,SeasonFactorid_id=factor,Countryid_id=country,Stateid_id=state,Month=month)
    user.save()
    messages.add_message(request,messages.INFO,"Added Succesfully")
    return render(request,'admin/adminhome.html')
def addagefactor(request):
    return render(request,"admin/addagefactor.html")
def addAction_AF(request):
    minage=request.POST['minage']
    maxage=request.POST['maxage']
    factor=request.POST['factorname']
    user=agefactor_tb(MinimumAge=minage,MaximumAge=maxage,Factorname=factor)
    user.save()
    messages.add_message(request,messages.INFO,"Added Succesfully")
    return render(request,'admin/adminhome.html')
def forgotpswd(request):
    return render(request,"common/forgotpswd.html")
def nextAction(request):
    username=request.POST['uname']
    user=register_tb.objects.filter(Username=username)
    if(user.count()>0):
        return render(request,"common/newpswd.html",{'us':username})
    else:
        messages.add_message(request,messages.INFO,"Invalid username")
        return redirect("login")
def nextAction2(request):
    username=request.POST['uname']
    name=request.POST['name']
    dob=request.POST['DOB']
    phnum=request.POST['phonenumber']
    user=register_tb.objects.filter(Name=name,DOB=dob,Phone=phnum)
    if(user.count()>0):
        return render(request,"common/changepswd.html",{'us':username})
    else:
        messages.add_message(request,messages.INFO,"Data is incorrect")
        return render(request,"common/index.html")
def resetAction(request):
    username=request.POST['uname']
    user=register_tb.objects.filter(Username=username)
    newpswd=request.POST['newpswd']
    confpswd=request.POST['confirmpswd']
    if(newpswd==confpswd):
        if(user.count()>0):
            user=register_tb.objects.filter(Username=username).update(Password=newpswd)
            messages.add_message(request,messages.INFO,"Reset successfull")
    else:
        messages.add_message(request,messages.INFO,"Password is incorrect")
    return render(request,"common/index.html")
def logout(request):
    request.session.flush()
    return redirect('index')

