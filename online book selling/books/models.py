from django.db import models
from django.urls import reverse
#creatin the manager for Book model 
class BookManager(models.Manager):
	def get_queryset(self):
		return super(BookManager,self).get_queryset().filter(available=True)
def upload_location(instance,filename):
	return '{}{}'.format(instance.book_name,filename)
	# Create your models here.
class Book(models.Model):
	BRANCH =(
	('Mechanical', 'Mechanical'),
	('Computer Science' ,'Computer Science'),
	( 'Information Science','Information Science'),
	('Chemical Engineering' ,'Chemical Engineering'),
	( 'Civil Engineering', 'Civil Engineering'),
	('Electrical Engineering' , 'Electrical Engineering'),
	('Electronic and Communication' , 'Electronic and Communication'),
	('Medical Electronics','Medical Electronics'),
	('Instrumentaion Engineering','Instrumentaion Engineering'),
	('Architecture','Architecture'),
	('Biotechnology','Biotechnology'))
	SEM =[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8)]
	#fields of book
	image 		= models.ImageField(upload_to=upload_location,blank=False,null=False)
	book_name	= models.CharField(max_length=100, null=False,blank=False)
	branch		= models.CharField(max_length=100, blank=False,null =False, choices=BRANCH)
	sem	  		= models.PositiveIntegerField(choices=SEM)
	price 		= models.PositiveIntegerField(blank=False , null=False)
	available 	= models.BooleanField(default=True)

	#Book's manager 
	objects = BookManager()
	#returning the unicode of the book
	def __str__(self):
			return self.book_name
	#getting the abslolute url 
	def get_absolute_url(self):
		return reverse('books:detail',kwargs={'id':self.id})



