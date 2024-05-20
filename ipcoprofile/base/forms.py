from django import forms
from django.contrib.auth import models






#...................................................................
class FindForm(forms.Form):
    find=forms.CharField()
    g1 = forms.BooleanField(required=False)
    g2 = forms.BooleanField(required=False)
    g3 = forms.BooleanField(required=False)
    g4 = forms.BooleanField(required=False)


class ShowForm(forms.Form):
    show=forms.CharField()
    g1 = forms.BooleanField(required=False)
    g2 = forms.BooleanField(required=False)
    g3 = forms.BooleanField(required=False)
    g4 = forms.BooleanField(required=False)




class DataForm(forms.Form):
    g1 = forms.BooleanField(required=False)
    g2 = forms.BooleanField(required=False)
    g3 = forms.BooleanField(required=False)
    g4 = forms.BooleanField(required=False)


class PartForm(forms.Form):
    part = forms.CharField(required=True)
    g1 = forms.BooleanField(required=False)
    g2 = forms.BooleanField(required=False)
    g3 = forms.BooleanField(required=False)
    g4 = forms.BooleanField(required=False)


