from django import forms
from models import Userpost

class Postform(forms.ModelForm):
	class Meta:
		model = Userpost
		fields = ('userpost_text',)
		#To improve set an error message if text get to 140 characters limit

class Deleteform(forms.ModelForm):
	class Meta:
		model = Userpost
		fields = []