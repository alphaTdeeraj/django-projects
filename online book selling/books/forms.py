from django import forms
from .models import Book
class BookForm(forms.ModelForm):
	class Meta:
		model 	= Book 
		fields	= ['image','book_name','branch','sem','price']
	# def clean_sem(self):
	# 	sem = self.cleaned_data.get('sem')
	# 	if sem>8:
	# 		raise forms.ValidationError('You have provided invalid Semester')
	# 	else:
	# 		return sem
	def clean_branch(self):
		branch = self.cleaned_data.get('branch')
		if not branch:
			raise forms.ValidationError('Please provide your branch')
		else:
			return branch
