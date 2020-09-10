from django import forms
from .models import Post, Category

# categories = [('Positive', 'Positive'), ('Negative', 'Negative')]
categories = Category.objects.all().values_list('name', 'name')

categories_list = []

for item in categories:
    categories_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'category')

        widgets = {
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your post title here! '}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'hayko', 'type':'hidden'}),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

