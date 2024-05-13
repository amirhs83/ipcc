from django import forms

class FormD(forms.Form):

    date = forms.CharField()



class FindForm(forms.Form):
    find=forms.CharField()


class ShowForm(forms.Form):
    show=forms.IntegerField()


class DataForm(forms.Form):
    g1 = forms.BooleanField(required=False)
    g2 = forms.BooleanField(required=False)
    g3 = forms.BooleanField(required=False)
    g4 = forms.BooleanField(required=False)


class PartForm(forms.Form):
    part = forms.IntegerField(required=True)
