from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class registerForm(forms.Form):
	name = forms.CharField(label="Name", min_length=2)
	alias = forms.CharField(label="Alias", min_length=2)
	email = forms.EmailField(label="Email")
	password = forms.CharField(widget=forms.PasswordInput, label="Password")
	conf_password = forms.CharField(widget=forms.PasswordInput, label="Confirm pw")

class loginForm(forms.Form):
	email = forms.EmailField(label="Email")
	password = forms.CharField(widget=forms.PasswordInput, label="Password")