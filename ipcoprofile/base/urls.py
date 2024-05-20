from django.urls import path, include
from .views import  home, AddDate, ShowCreate, InputShow, Data_2, DeletDay, Upload, UserRegister,LoginUser,UserLogout

urlpatterns = [
 path("", home, name="home"),
 path('show/',InputShow.as_view(),name="show"),


 path('adddate/',AddDate.as_view(),name='adddate'),
 path('showcreate/',ShowCreate.as_view(),name='showcreate'),
 path('showbar2/',Data_2.as_view(),name='showbar2'),
 path('deleteday/<int:id>/',DeletDay.as_view(),name='deletday'),
 path('uploadfile/',Upload.as_view(),name='uploadfile'),
 path('userregister/',UserRegister.as_view(),name='userregister'),
 path('userlogin/',LoginUser.as_view(),name='loginuser'),
 path('userlogout/',UserLogout.as_view(),name='userlogout'),

]