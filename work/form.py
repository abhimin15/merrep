from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import extras
from django.contrib.admin.widgets import AdminDateWidget
from functools import partial
from django.utils.safestring import mark_safe
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from .models import *
class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Email'}))
    sex = forms.ChoiceField(widget=forms.Select(attrs={'class': 'sex', 'required': 'true', 'placeholder': 'Sex', }),
                            choices=sex_choices, )

    year = forms.ChoiceField(widget=forms.Select(attrs={'class': 'year', 'required': 'true', 'placeholder': 'Year', }),
                             choices=year_choices, )

    class Meta:
        model = User
        fields = ['username','email','sex','year','password1','password2']

class ContactForm(forms.ModelForm):

    class Meta:
        model = contact
        fields = ['name','email','number','message']
class OrderForm(forms.ModelForm):
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'class':'form-control','required':'true','placeholder':'Email'}))
    amount = forms.DecimalField(decimal_places=2)
    class Meta:
        model = Profile
        fields = ['user','email','amount']

class paymentForm(forms.Form):
	delegateOption=(('Indian Delegate', 'Indian Delegate',),('Foreign Delegate', 'Foreign Delegate',),)
	delegate = forms.ChoiceField(widget=forms.Select(attrs={'class' : 'form-control','id':'delegate'}),choices=delegateOption)
	persons_count = forms.IntegerField(widget=forms.NumberInput(attrs={'class' : 'form-control','id':'persons_count'}),min_value=1,max_value=6,required=True)
	person1=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'person1','readonly':'readonly'}), max_length=50)

	person2=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'person2'}), max_length=50,required=False)
	person3=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'person3'}), max_length=50,required=False)
	person4=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'person4'}), max_length=50,required=False)
	person5=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'person5'}), max_length=50,required=False)
	person6=forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'person6'}), max_length=50,required=False)
	terms=forms.MultipleChoiceField(widget=forms.CheckboxInput(attrs={'id':'termsPay','value':"I abide by the <a>terms and conditions</a>"}),required=True)
