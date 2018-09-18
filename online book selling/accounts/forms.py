from django import forms
from django.contrib.auth import  get_user_model ,login , authenticate
User = get_user_model()
#creating the user registration forms
class RegisterForm(forms.ModelForm):
	password1 = forms.CharField(label='Password',widget=forms.PasswordInput,required=True)
	password2 = forms.CharField(label='password confirmation',widget=forms.PasswordInput,required=True)
	class Meta:
		model = User
		fields = ['name','email']

	#def cleaning the data which is coming from the forms 
	def clean_password2(self):
		# Check that the two password entries match
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match")
		return password2

	def save(self,commit=True):
		user = super(RegisterForm,self).save(commit=False)
		user.set_password(self.cleaned_data.get('password1'))
		if commit:
			user.save()
		return user

#creating the class for loging in the user 
class LoginForm(forms.Form):
	email = forms.EmailField(required=True,label='Eamil')
	password = forms.CharField(required=True,widget=forms.PasswordInput,label='Password')

	def __init__(self,request,*args ,**kwargs):
		self.request = request
		print(self.request)
		return super(LoginForm,self).__init__(*args,**kwargs)
