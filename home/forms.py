from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.admin.widgets import AdminDateWidget



class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name' , 'email', 'password1', 'password2')
class ForgotpasswordForm(forms.Form):
	username=forms.CharField(max_length=100)
	email=forms.EmailField(max_length=100)

	def clean(self):
		cleaned_data=super(ForgotpasswordForm,self).clean()
		Username=cleaned_data.get('Username')
        # email=cleaned_data.get('email')