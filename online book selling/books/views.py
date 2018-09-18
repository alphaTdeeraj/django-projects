from django.shortcuts import render , get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from .forms import BookForm
from .models import Book 

# Create your views here.

class BookListView(ListView):
	model = Book
	queryset = Book.objects.all()
	template_name = 'book.html'
	#definig a method to handle the get method

#function based views for creating the new_book
def sell_book(request):
	form = BookForm(request.POST or None,request.FILES or None )
	if request.method=='POST' and form.is_valid():
		form.save(commit=True)
	context = {'form':form}
	return render(request, 'create_book.html',context)


#creating the detail of book with commet section
def detail_book(request,id):
	obj = get_object_or_404(Book,id=id)
	print(obj)
	context = {'obj':obj}
	return render(request, "detail_book.html",context)

#method for getting the query set from the data base and get the use
# def search(request):
# 	query = request.GET.get("q")
# 	#i'm dealing with the multiple of fields in the database 
# 	qs = Book.objects.filter(name__icontains=query)
# 	context = {'qs':qs}
# 	return render(request,'book.html',context)
def search(request):
	look_up = request.GET.get('q')
	context = {'object_list':None}
	if  look_up:
		qs = Book.objects.filter(book_name__icontains=look_up)
		context['inform'] = '{} book(s) found with name containg {}'.format(len(qs),look_up)
		qs = Book.objects.all()
	else:
		qs = Book.objects.all()
	context['object_list'] = qs
	return render(request,'book.html',context)
		