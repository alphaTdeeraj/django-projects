from django.urls import path 
from .views import (login , register,logout )

#attribute of app_name 
app_name = 'accounts'
#write the list of url patters 
urlpatterns = [
				path('login/', login,name='login'),
				path('register/', register,name='register'),
				path('logout/', logout,name='logout'),

	]