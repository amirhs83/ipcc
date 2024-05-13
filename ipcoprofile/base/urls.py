from django.urls import path, include
from .views import authView, home, Calender,DeleteDate,AddDate,ShowCreate,InputShow,AllDays,Data_2,Data



urlpatterns = [
 path("", home, name="home"),
 path('show/',InputShow.as_view(),name="show"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
 path("calender/",Calender.as_view(), name="calendar"),
 path("viewdate/",DeleteDate.as_view(),name='deletedate'),
 path('adddate/',AddDate.as_view(),name='adddate'),
 path('showcreate/',ShowCreate.as_view(),name='showcreate'),
 path('alldays/',AllDays.as_view(),name='alldays'),
 path("showbar/",Data.as_view(),name='showbar'),
 path('showbar2/',Data_2.as_view(),name='showbar2'),
]