from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter author name'}),
            'price': forms.NumberInput(attrs={'min': 0, 'max': 1000}),
            'edition': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'price': 'Price',
            'edition': 'Edition',
        }
