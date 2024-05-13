from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
import pandas as pd
import sqlite3
from .pandasff import eskelet,en
from .forms import FormD,FindForm,ShowForm,DataForm,PartForm
from .models import Date
import pandas as pd
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from datetime import datetime, timedelta
from .models import Date


@login_required
def home(request):
    date = Date.objects.all()








    return render(request,"home.html",{"date":date})

class Calender(View):
    def get(self,request):
        form = FormD()
        return render(request, "calender.html",{"form":form})

    def post(self,request):
        form = FormD(request.POST)
        if form.is_valid():

            df = pd.read_csv("ipcodate.csv")
            cd = form.cleaned_data["date"]
            ds = pd.Series([cd], name="daysoff")
            df = df.assign(daysoff = ds)

            return render(request, "calender.html",{"df":df})
        else:
            return None






def authView(request):
 if request.method == "POST":
  form = UserCreationForm(request.POST or None)
  if form.is_valid():
   form.save()
   return redirect("base:login")
 else:
  form = UserCreationForm()
 return render(request, "registration/signup.html", {"form": form})

# Create your views here.
class DeleteDate(View):
    def get(self,request):
        form=FindForm()

        return render(request,'viewdates.html',{"form":form})
    def post(self,request):
        form=FindForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            date=Date.objects.get(name=cd["find"])
            date.delete()
        return render(request,'viewdates.html',{"form":form})

class AddDate(View):
    def get(self,request):
        form=FormD()
        return render(request,"adddate.html",{"form":form})

    def post(self,request):
        form=FormD(request.POST)
        if form.is_valid():
            cd=form.cleaned_data

            date=Date(name=cd["date"])
            date.save()

            return render(request,"adddate.html",{"form":form})



class ShowCreate(View):
    def get(self,request):
        dfbom = pd.read_csv('bom.csv')
        dfbom = pd.DataFrame(dfbom)
        days = Date.objects.all()
        daysoff = []
        for i in days:
            daysoff.append(i.name)

        dates = [datetime.today() + timedelta(days=i) for i in range(11)]
        dates_str = [date.strftime('%Y-%m-%d') for date in dates]
        for i in dates_str:
            if i in daysoff:
                dates_str.remove(i)


        dfdaycreate = pd.read_csv('daycreate.csv')
        dfdaycreate = pd.DataFrame(dfdaycreate)

        dfdaycreate = dfdaycreate.mul(dfbom.iloc[0])

        for a in range(0, len(dfdaycreate) - 1):
            sum_row = dfdaycreate.iloc[a].sum()

            dfdaycreate.iloc[a + 1, 0] = sum_row

        dfdaycreate["sumcreate"] = dfdaycreate.sum(axis=1)

        dfdaycreate["dateon"] = pd.DataFrame({'dates': dates_str})

        return render(request,"showcreate.html",context={"dfdaycreate":dfdaycreate,"days":days})
    def post(self,request):
        pass

class InputShow(View):
    def get(self,request):
        form=ShowForm()




        return render(request,'inputshow.html',{'form':form})


    def post(self,request):
        form=ShowForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            tolid,llist,gg,dd,gomrock,tolidd=eskelet(int(cd['show']))
            x=[]
            df = pd.DataFrame(tolid)
            htmlt = df.to_html(classes='table table-striped')
            for i in range(0,len(tolid)):
                x.append(i)

            return render(request,'inputshow.html',{'htmlt':htmlt,'form':form})


class AllDays(View):
    def get(self,request):
        dfbook = pd.read_csv('Book1.csv')
        dfbook = pd.DataFrame(dfbook)
        dddd={}
        for i in range(0,len(dfbook)-1):
            dddd[i]=eskelet(int(i))[1]
        return render(request,'alldays.html',{'dddd':dddd})

    def post(self,request):

        pass


class Data(View):

    def get(self, request):
        form = DataForm

        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = DataForm(request.POST)

        if form.is_valid():


            cd = form.changed_data
            if cd == []:
                msg = 'required'
                return render(request, 'form.html', {'form': form, 'msg': msg})
            else:
                labels,data=en(cd)




                return render(request, 'form.html', {'form': form,'labels':labels,'data':data})


class Data_2(View):
    def get(self,request):
        form=PartForm
        return render(request,'showbar_2.html',{'form':form})

    def post(self,request):
        form = PartForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            dd,ff, labels_2,data_2,cc,gg=eskelet(int(cd['part']))
            return render(request,'showbar_2.html',{'labels_2':labels_2,'data_2':data_2,'form':form})

