from django.urls import path 
from .views import (BookListView, sell_book , detail_book,search)

app_name = 'books'
#creating the list of url patterns 
urlpatterns = [
				path('',BookListView.as_view(), name='list'),
				path('sellbook/', sell_book, name='sell'),
				path('<int:id>/', detail_book , name='detail'),
				path('search/', search , name='search'),


				]