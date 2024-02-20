from django.shortcuts import render,redirect
from Site_admin.models import *
from user.models import *
from django.contrib import messages
from django.http import JsonResponse
import datetime

def register(request):
    hobby=hobbyname_tb.objects.all()
    country=country_tb.objects.all()
    return render(request,'user/register.html',{'co':country,'ho':hobby})
def getstate(request):
    countryid=request.GET['co']
    state=state_tb.objects.filter(Country_id_id=countryid)
    return render(request,'user/getstate.html',{'st':state})
def registerAction(request):

    name=request.POST['name']
    gender=request.POST['gender']
    DOB=request.POST['DOB']
    address=request.POST['address']
    country=request.POST['country']
    state=request.POST['state']
    phone=request.POST['phone']
    hobby=request.POST.getlist('hobby')
    question=request.POST['question']
    ans=request.POST['answer']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb(Name=name,Gender=gender,DOB=DOB,Address=address,Countryid_id=country,Stateid_id=state,Phone=phone,SecurityQuestion=question,Answer=ans,Username=username,Password=password)
    user.save()
    id=user[0].id
    for i in hobby:
        hobbies=hobby_tb(Hobbyid_id=i,Userid_id=id)
        hobbies.save()
    messages.add_message(request,messages.INFO,"Registration was suucessfull")
    return render(request,"common/index.html")
def sendmessage(request):
    return render(request,"user/sendmessage.html")
def checkemail(request):
    receiver=request.GET['re']
    user=register_tb.objects.filter(Username=receiver)
    if(user.count()>0):
        msg='exist'
    else:
        msg='notexist'
    return JsonResponse({'valid':msg})
def sendAction(request):
    sid=request.session['user_id']
    subject=request.POST['subject']
    message=request.POST['message']
    Date=datetime.date.today()
    Time=datetime.datetime.now().strftime("%H:%M")
    receiver=request.POST['receiver']
    recvr=register_tb.objects.filter(Username=receiver)
    rid=recvr[0].id
    user=message_tb(Senderid_id=sid,Receiverid_id=rid,Subject=subject,Message=message,Date=Date,Time=Time)
    user.save()
    messages.add_message(request,messages.INFO,"Message sent")
    return render(request,"user/userhome.html")
def viewSentmessage(request):
    sid=request.session['user_id']
    user=message_tb.objects.filter(Senderid_id=sid)
    return render(request,"user/viewSentmessage.html",{'se':user})
def delete(request,id):
    user=message_tb.objects.filter(id=id).update(Status="Deleted by sender")
    return render(request,"user/userhome.html")
def viewReceivedmessage(request):
    id=request.session['user_id']
    Status=["Pending","Deleted by sender"]
    agefactor=Customeragefactor_tb.objects.filter(Userid_id=id)
    for factor in agefactor:
        msg=message_tb.objects.filter(Receiverid_id=id,FilterStatus="Pending",Message__icontains=factor.Factorid.Factorname).exclude(Senderid_id__in=Blocklist_tb.objects.filter(Userid_id=id).values('Contactid')).update(FilterStatus='Filtered')
    hobbyfactor=Customerhobby_tb.objects.filter(Userid_id=id)
    for factor2 in hobbyfactor:
        msg2=message_tb.objects.filter(Receiverid_id=id,FilterStatus="Pending",Message__icontains=factor.Factorid.Factorname).exclude(Senderid_id__in=Blocklist_tb.objects.filter(Userid_id=id).values('Contactid')).update(FilterStatus='Filtered')
    seasonfactor=CustomerSeasoncountry_tb.objects.filter(Userid_id=id)
    for factor3 in seasonfactor:
        msg3=message_tb.objects.filter(Receiverid_id=id,FilterStatus="Pending",Message__icontains=factor.Factorid.Factorname).exclude(Senderid_id__in=Blocklist_tb.objects.filter(Userid_id=id).values('Contactid')).update(FilterStatus='Filtered')
    view=message_tb.objects.filter(Receiverid_id=id,FilterStatus='Filtered',Status__in=Status).exclude(id__in=trash_tb.objects.filter(Receiverid_id=id).values('Messageid_id'))
    # user=message_tb.objects.filter(Receiverid_id=id)
    return render(request,"user/receivedmessage.html",{'re':view})
def trashAction(request):
    mid=request.POST.getlist('mid')
    id=request.session['user_id']
    for i in mid:
        date=datetime.date.today()
        time=datetime.datetime.now().strftime("%H:%M")
        user=trash_tb(Receiverid_id=id,Messageid_id=i,Date=date,Time=time)
        user.save()
    messages.add_message(request,messages.INFO,"Moved to Trash")
    return render(request,"user/userhome.html")
def viewTrash(request):
    id=request.session['user_id']
    user=trash_tb.objects.filter(Receiverid_id=id)
    for i in user:
        mid=user[0].Messageid_id
        msg=message_tb.objects.filter(id=mid)
        sid=msg[0].Senderid_id
        name=register_tb.objects.filter(id=sid)
    return render(request,"user/viewTrash.html",{'a':msg,'na':name})
def deleteTrash(request,id):
    user=message_tb.objects.filter(id=id)
    status=user[0].Status
    if (status=="Pending"):
        msg=message_tb.objects.filter(id=id).update(Status="Deleted by receiver")
        msg=trash_tb.objects.filter(Messageid_id=id).delete()
    return render(request,"user/userhome.html")
def forward(request,id):
    msg=message_tb.objects.filter(id=id)
    return render(request,"user/forward.html",{'m':msg})
def forwardAction(request):
    sid=request.session['user_id']
    subject=request.POST['subject']
    message=request.POST['msg']
    remail=request.POST['r_email']
    user=register_tb.objects.filter(Username=remail)
    rid=user[0].id
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    msg=message_tb(Senderid_id=sid,Receiverid_id=rid,Subject=subject,Message=message,Date=date,Time=time)
    msg.save()
    messages.add_message(request,messages.INFO,"Message sent")
    return render(request,"user/userhome.html")
def reply(request,id):
    msg=message_tb.objects.filter(id=id)
    sid=msg[0].Senderid_id
    user=register_tb.objects.filter(id=sid)
    return render(request,"user/reply.html",{'a':user})
def ReplyAction(request):
    sid=request.session['user_id']
    subject=request.POST['subject']
    message=request.POST['msg']
    remail=request.POST['r_email']
    user=register_tb.objects.filter(Username=remail)
    rid=user[0].id
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    msg=message_tb(Senderid_id=sid,Receiverid_id=rid,Subject=subject,Message=message,Date=date,Time=time)
    msg.save()
    messages.add_message(request,messages.INFO,"Message sent")
    return render(request,"user/userhome.html")
def addcontact(request):
    return render(request,"user/addcontact.html")
def addcontactAction(request):
    id=request.session['user_id']
    contact=request.POST['contact']
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=register_tb.objects.filter(Username=contact)
    cid=user[0].id
    cont=Contact_tb(Name=name,Contactid_id=cid,Remarks=remarks,Date=date,Time=time,Userid_id=id)
    cont.save()
    messages.add_message(request,messages.INFO,"Contact saved")
    return render(request,"user/userhome.html")
def blocklist(request):
    return render(request,"user/blocklist.html")
def addtoblocklist(request):
    id=request.session['user_id']
    contact=request.POST['contact']
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    user=register_tb.objects.filter(Username=contact)
    cid=user[0].id
    cont=Blocklist_tb(Name=name,Contactid_id=cid,Remarks=remarks,Date=date,Time=time,Userid_id=id)
    cont.save()
    messages.add_message(request,messages.INFO,"Added to blocklist")
    return render(request,"user/userhome.html")
def viewcontact(request):
    id=request.session['user_id']
    contact=Contact_tb.objects.filter(Userid_id=id)
    cid=contact[0].Contactid_id
    user=register_tb.objects.filter(id=cid)
    return render(request,"user/viewcontact.html",{'c':contact,'u':user})
def Delete(request,id):
    user=Contact_tb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Deleted")
    return render(request,"user/userhome.html")
def movetoblocklist(request,id):
    
    blklist=Contact_tb.objects.filter(id=id)
    name=blklist[0].Name
    Date=blklist[0].Date
    Time=blklist[0].Time
    remarks=blklist[0].Remarks
    cid=blklist[0].Contactid_id
    uid=blklist[0].Userid_id
    user_2=Blocklist_tb(Name=name,Contactid_id=cid,Remarks=remarks,Date=Date,Time=Time,Userid_id=uid)
    user_2.save()
    user=Contact_tb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Added to blocklist")
    return render(request,"user/userhome.html")
def viewblocklist(request):
    id=request.session['user_id']
    blocklist=Blocklist_tb.objects.filter(Userid_id=id)
    cid=blocklist[0].Contactid_id
    user=register_tb.objects.filter(id=cid)
    return render(request,"user/viewblocklist.html",{'c':blocklist,'u':user})
def DeleteBL(request,id):
    user=Blocklist_tb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Deleted")
    return render(request,"user/userhome.html")
def addcustomerhobby(request):
    hobby=hobbyname_tb.objects.all()
    return render(request,"user/addcustomerhobby.html",{'h':hobby})
def getfactor(request):
    hobbyid=request.GET['h']
    factor=hobbyfactor_tb.objects.filter(Hobby_id_id=hobbyid)
    return render(request,'user/getfactor.html',{'f':factor})
def addAction(request):
    uid=request.session['user_id']
    hid=request.POST['hobby']
    fid=request.POST['factor']
    user=Customerhobby_tb(Userid_id=uid,Hobbyid_id=hid,Factorid_id=fid)
    user.save()
    messages.add_message(request,messages.INFO,"Added Succesfully")
    return render(request,'admin/adminhome.html')
def addcustomeragefactor(request):
    factor=agefactor_tb.objects.all()
    return render(request,'user/addcustomeragefactor.html',{'f':factor})
def AddActionAF(request):
    sid=request.session['user_id']
    fid=request.POST['factor']
    user=Customeragefactor_tb(Factorid_id=fid,Userid_id=sid)
    user.save()
    messages.add_message(request,messages.INFO,"Added Succesfully")
    return render(request,"user/userhome.html")
def addcustomerseasoncountry(request):
    id=request.session['user_id']
    user=register_tb.objects.filter(id=id)
    country=user[0].Countryid_id
    state=user[0].Stateid_id
    date=datetime.date.today()
    Month=date.month
    factor=seasoncountry_tb.objects.filter(Countryid_id=country,Stateid_id=state,Month=Month)
    return render(request,'user/addcustomerseasoncountry.html',{'f':factor})
def viewspam(request):
    id=request.session['user_id']
    user=message_tb.objects.filter(Receiverid_id=id,Status="Deleted by sender" or "Pending",FilterStatus="Pending")
    return render(request,"user/viewspam.html",{'re':user})
def delete_spam(request,id):
    user=message_tb.objects.filter(id=id)
    if (user.Status=="Deleted by sender"):
        msg=message_tb.objects.filter(id=id).delete()
    else:
        msg=message_tb.objects.filter(id=id).update(Status="Deleted by Receiver")
def AddActionSF(request):
    sid=request.session['user_id']
    fid=request.POST['factor']
    user=CustomerSeasoncountry_tb(Factorid_id=fid,Userid_id=sid)
    user.save()
    messages.add_message(request,messages.INFO,"Added Succesfully")
    return render(request,"user/userhome.html")
def updateprofile(request):
    id=request.session['user_id']
    hobby=hobbyname_tb.objects.all()
    userhobby=hobby_tb.objects.filter(Userid_id=id)
    country=country_tb.objects.all()
    user=register_tb.objects.filter(id=id)
    return render(request,"user/updateprofile.html",{'us':user,'co':country,'ho':hobby,'uho':userhobby})
def getstate2(request):
    countryid=request.GET['co']
    state=state_tb.objects.filter(Country_id_id=countryid)
    return render(request,'user/getstate2.html',{'st':state})
def updateAction(request):
    id=request.session['user_id']
    name=request.POST['name']
    gender=request.POST['gender']
    DOB=request.POST['DOB']
    address=request.POST['address']
    country=request.POST['country']
    state=request.POST['state']
    phone=request.POST['phone']
    hobby=request.POST.getlist('hobby')
    question=request.POST['question']
    ans=request.POST['answer']
    username=request.POST['username']
    password=request.POST['password']
    user=register_tb.objects.filter(id=id).update(Name=name,Gender=gender,DOB=DOB,Address=address,Countryid_id=country,Stateid_id=state,Phone=phone,SecurityQuestion=question,Answer=ans,Username=username,Password=password)
    for i in hobby:

        hobbies=hobby_tb.objects.filter(Userid_id=id).update(Hobbyid_id=i,Userid_id=id)
        
    messages.add_message(request,messages.INFO,"Updation was suucessfull")
    return render(request,"common/index.html")
def ResetPassword(request):
    return render(request,"user/ResetPassword.html")
def resetAction_user(request):
    id=request.session["user_id"]
    user=register_tb.objects.filter(id=id)
    oldpswd=request.POST['oldpswd']
    newpswd=request.POST['newpswd']
    confpswd=request.POST['confirmpswd']
    if(user[0].Password == oldpswd):
        if(newpswd == confpswd):
            newpass=register_tb.objects.filter(id=id).update(Password=newpswd)
            messages.add_message(request,messages.INFO,"Reset successfull")
        else:
            messages.add_message(request,messages.INFO,"Password does not match")  
    else:
        messages.add_message(request,messages.INFO,"Password is incorrect") 
        
    return render(request,"common/index.html")
def home_user(request):
    return render(request,"user/userhome.html")
def logout(request):
    request.session.flush()
    return redirect('index')




