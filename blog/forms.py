from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title', 'content', 'featured_image', 'Category', 'author']
        widgets = {
            'content': forms.Textarea(attrs={'rows':10})
        }
        help_text = {
            'title': 'The URL of slug is auto-generated from the title.'
        }

        def clean_title(self):
            title = self.cleaned_data['title'].strip()
            if len(title) < 5:
                raise ValidationError('Use a real title')
            return title
