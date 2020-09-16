from django import forms
from .models import Exchange

class Myform(forms.ModelForm):
	class Meta:
		model = Exchange
		fields = '__all__'