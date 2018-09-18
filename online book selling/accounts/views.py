from django.shortcuts import reverse , render ,redirect
from .forms import RegisterForm , LoginForm
from django.contrib.auth import login as auth_login , logout as auth_logout
from django.contrib.auth import authenticate


def register(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid() and request.method=="POST":
		email =form.cleaned_data.get('email')
		password = form.cleaned_data.get('password2')
		user = authenticate(request,username=email,password=password1)
		if user:
			auth_login(request,user)
			return redirect('books:list')
	context = {'form':form}
	return render(request,'register.html',context)

def login(request):
	form = LoginForm(request.POST or None)
	context = {'form':form,'fail':None}
	if request.method=="POST":
		print('enterd the valid statement in view')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(request,username=email,password=password)
		if user:
			auth_login(request,user)
			return redirect(reverse('books:list'))
		else:
			context['fail'] = True
	return render(request,'login.html',context)


def logout(request):
	auth_logout(request)
	return redirect(reverse('books:list'))

	






