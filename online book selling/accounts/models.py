from django.contrib.auth.models  import (AbstractBaseUser, BaseUserManager)
from django.db import models 
#creating the manager of the User model 
class UserManager(BaseUserManager):
	#method for creating the User model
	def create_user(self,name,email,password=None,is_active=True,is_staff=False,is_admin=False):
		if not name:
			raise ValueError('User must have a name')
		if not email:
			raise ValueError('User must have a email address')
		if not password:
			raise ValueError('User must have a password')
		User = self.model(name=name,email=self.normalize_email(email))
		User.set_password(password)
		# User.active = is_active
		User.staff  = is_staff
		User.admin  = is_admin
		#save the model using the save method which is provided by the  BaseUserManager
		User.save(using=self._db)
		return User
	#method for creatin the staff 
	def create_staff(self,name,email,password=None):
		User = self.create_user(name,email,password=password,is_staff=True)
		return User

	#method for creating the adming
	def create_superuser(self,name,email,password=None):
		User = self.create_user(name,email,password=password,is_staff=True,is_admin=True)
		return User

#creating the custom user model 
class User(AbstractBaseUser):
	name 		= models.CharField(max_length=100,null=False,blank=False)
	email		= models.EmailField(max_length=255,unique=True,null=False,blank=False)
	active		= models.BooleanField(default=True)
	staff 		= models.BooleanField(default=False)
	admin		= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'#overide the username of the parent class 
	REQUIRED_FIELDS = ['name'] #it will be runned when you create the use object
	#the representation of the class 
	objects = UserManager()
	def __str__(self):
		return self.email

	#methods for getting the fields of the model 
	def get_name(self):
		if self.name:
			return self.name
		else:
			return self.email

	def get_email(self):
		return self.email
	#creating some of the property decorator 
	# @property
	# def is_active(self):
	# 	return self.active
	def has_module_perms(self,app_label):
		return True
	def has_perm(self,perm,obj=None):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin
	