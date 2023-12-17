from django import forms
from .models import Book, Dog

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'content']