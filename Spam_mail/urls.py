"""
URL configuration for Spam_mail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from Site_admin import views as adminview
from user import views as userview
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name="index"), 
    path('login/',adminview.login,name="login"),
    path('loginAction/',adminview.loginAction,name="loginAction"),
    path('addhobby/',adminview.addhobby,name="addhobby"),
    path('SaveAction/',adminview.SaveAction,name="SaveAction"),
    path('addhobbyfactor/',adminview.addhobbyfactor,name="addhobbyfactor"),
    path('saveAction/',adminview.saveAction,name="saveAction"),
    path('addseason/',adminview.addseason,name="addseason"),
    path('SaveAction_season/',adminview.SaveAction_season,name="SaveAction_season"),
    path('addseasonfactor/',adminview.addseasonfactor,name="addseasonfactor"),
    path('saveAction_seasonfactor/',adminview.saveAction_seasonfactor,name="saveAction_seasonfactor"),
    path('logout/',adminview.logout,name="logout"),
    path('register/',userview.register,name="register"),
    path('getstate/',userview.getstate,name="getstate"),
    path('registerAction/',userview.registerAction,name="registerAction"),
    path('sendmessage/',userview.sendmessage,name="sendmessage"),
    path('checkemail/',userview.checkemail,name="checkemail"),
    path('sendAction/',userview.sendAction,name="sendAction"),
    path('viewSentmessage/',userview.viewSentmessage,name="viewSentmessage"),
    path('delete<int:id>/',userview.delete,name="delete"),
    path('viewReceivedmessage/',userview.viewReceivedmessage,name="viewReceivedmessage"),
    path('trashAction/',userview.trashAction,name="trashAction"),
    path('viewTrash/',userview.viewTrash,name="viewTrash"),
    path('deleteTrash<int:id>/',userview.deleteTrash,name="deleteTrash"),
    path('forward<int:id>/',userview.forward,name="forward"),
    path('forwardAction/',userview.forwardAction,name="forwardAction"),
    path('reply<int:id>/',userview.reply,name="reply"),
    path('ReplyAction/',userview.ReplyAction,name="ReplyAction"),
    path('addcontact/',userview.addcontact,name="addcontact"),
    path('addcontactAction/',userview.addcontactAction,name="addcontactAction"),
    path('blocklist/',userview.blocklist,name="blocklist"),
    path('addtoblocklist/',userview.addtoblocklist,name="addtoblocklist"),
    path('viewcontact/',userview.viewcontact,name="viewcontact"),
    path('Delete<int:id>/',userview.Delete,name="Delete"),
    path('logout/',userview.logout,name="logout"),
    path('movetoblocklist<int:id>/',userview.movetoblocklist,name="movetoblocklist"),
    path('viewblocklist/',userview.viewblocklist,name="viewblocklist"),
    path('DeleteBL<int:id>/',userview.DeleteBL,name="DeleteBL"),
    path('addcustomerhobby/',userview.addcustomerhobby,name="addcustomerhobby"),
    path('getfactor/',userview.getfactor,name="getfactor"),
    path('addseasoncountry/',adminview.addseasoncountry,name="addseasoncountry"),
    path('getseasonfactor/',adminview.getseasonfactor,name="getseasonfactor"),
    path('getstate_SC/',adminview.getstate_SC,name="getstate_SC"),
    path('addAction_SC/',adminview.addAction_SC,name="addAction_SC"),
    path('addAction/',userview.addAction,name="addAction"),
    path('addagefactor/',adminview.addagefactor,name="addagefactor"),
    path('addAction_AF/',adminview.addAction_AF,name="addAction_AF"),
    path('addcustomeragefactor/',userview.addcustomeragefactor,name="addcustomeragefactor"),
    path('AddActionAF/',userview.AddActionAF,name="AddActionAF"),
    path('addcustomerseasoncountry/',userview.addcustomerseasoncountry,name="addcustomerseasoncountry"),
    path('viewspam/',userview.viewspam,name="viewspam"),
    path('delete_spam<int:id>/',userview.delete_spam,name="delete_spam"),
    path('AddActionSF/',userview.AddActionSF,name="AddActionSF"),
    path('updateprofile/',userview.updateprofile,name="updateprofile"),
    path('updateAction/',userview.updateAction,name="updateAction"),
    path('forgotpswd/',adminview.forgotpswd,name="forgotpswd"),
    path('nextAction/',adminview.nextAction,name="nextAction"),
    path('nextAction2/',adminview.nextAction2,name="nextAction2"),
    path('resetAction/',adminview.resetAction,name="resetAction"),
    path('ResetPassword/',userview.ResetPassword,name="ResetPassword"),
    path('resetAction_user/',userview.resetAction_user,name="resetAction_user"),
    path('home_user/',userview.home_user,name="home_user")




]
