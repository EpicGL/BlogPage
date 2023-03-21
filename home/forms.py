from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','author']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'author': forms.HiddenInput()

        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','comment', 'post']