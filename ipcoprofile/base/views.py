from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View

from .pandasff import eskelet,en
from .forms import FindForm,ShowForm,DataForm,PartForm

import pandas as pd
from django.contrib.auth.models import User

from datetime import datetime, timedelta
from .models import Date

import os
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    date = Date.objects.all()

    return render(request,"base.html",{"date":date})



class UserRegister(View):
    def get(self,request):
        pass



    def post(self,request):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect("base:home")

class UserLogout(View):
    def get(self,request):
        logout(request)
        messages.success(request,"You have been loggedout")
        return redirect("base:home")
    def post(self,request):
        pass
class LoginUser(View):
    def get(self,request):
        pass
    def post(self,request):
        username = request.POST.get("username")

        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=username,email=email, password=password)
        if user is not None:
            login(request,user)

        return redirect("base:home")



class Upload(LoginRequiredMixin,View):
    login_url = '/'



    def get(self,request):
        return render(request,'upload.html')


    def post(self,request):
        file=request.FILES.get("fileupload")
        filename = file.name

        file_content = file.read()
        with open(os.path.join(r'C:\Users\amirhs\PycharmProjects\ipcoprofile', filename), 'wb') as f:
            f.write(file_content)


        return render(request,'upload.html',{"file":file})



class AddDate(LoginRequiredMixin,View):
    login_url = '/'

    def get(self,request):
        days=Date.objects.all()

        return render(request,"adddate.html",{'days':days})

    def post(self,request):

        date1 = request.POST.get('adddate')
        days=Date.objects.all()


        if len(date1) == 10:



            date=Date(name=str(date1))
            date.save()
            msg = 'روز با موفقیت اضافه شد'
        else:
            msg='نباید خالی باشد'


        return render(request,"adddate.html",{'msg':msg,'days':days,'date1':date1})



class ShowCreate(LoginRequiredMixin,View):
    login_url = '/'
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

class InputShow(LoginRequiredMixin,View):
    login_url = '/'
    def get(self,request):
        form=ShowForm()

        return render(request,'inputshow.html',{'form':form})

    def post(self,request):
        form=ShowForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            listf=[]
            for j in cd:
                if cd[str(j)] == True:
                    listf.append(str(j))

            tolid,llist,gg,dd,gomrock,tolidd=eskelet(str(cd['show']),listf)
            x=[]
            df = pd.DataFrame(tolid)
            htmlt = df.to_html(classes='table table-striped')
            for i in range(0,len(tolid)):
                x.append(i)


            return render(request,'inputshow.html',{'htmlt':htmlt,'form':form,'listf':listf})


class Data_2(LoginRequiredMixin,View):
    login_url = '/'
    def get(self,request):
        form=PartForm
        return render(request,'showbar_2.html',{'form':form})

    def post(self,request):
        form = PartForm(request.POST)
        listf=[]


        if form.is_valid():

            cd = form.cleaned_data
            for j in cd:
                if cd[str(j)] == True:
                    listf.append(str(j))
            dd,ff, labels_2,data_2,cc,gg=eskelet(str(cd['part']),listf)
            return render(request,'showbar_2.html',{'labels_2':labels_2,'data_2':data_2,'form':form,'listf':listf})


class DeletDay(View):
    def get(self,request,id):
        day = Date.objects.get(id=id)
        day.delete()
        return redirect('base:adddate')

    def post(self,request,id):
        pass
