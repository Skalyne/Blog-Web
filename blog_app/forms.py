from django import forms
from .models import Post, Category, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','header_image','title_tag','category','author','body')

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the post title'}),
            'title_tag': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','id':'elder', 'type': 'hidden',}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','header_image','title_tag','body','category')

        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write Your Name'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body',)

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write the post title'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            
        }