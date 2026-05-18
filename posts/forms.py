from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:

        model = Post

        fields = ['title', 'content', 'category', 'tags', 'image', 'is_published']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Post title'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6,
                    'placeholder': 'Write your post content...'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'tags': forms.CheckboxSelectMultiple(
                attrs={
                    'class': 'form-check-input'
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'is_published': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            )
        }
