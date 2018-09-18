from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'branch','sem','price']
admin.site.register(Book ,BookAdmin )