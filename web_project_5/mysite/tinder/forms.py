from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddPost(forms.Form):
    title = forms.CharField(label='Your title', max_length=20)
    body = forms.CharField(label="body")

    def clean_title(self):
        if 'title' in self.cleaned_data:
            title = self.cleaned_data['title']
            return title

    def clean_body(self):
        if 'body' in self.cleaned_data:
            body = self.cleaned_data['body']
            return body

    def save(self):
        Post.objects.create(title=self.cleaned_data['title'], body=self.cleaned_data['body'], date=timezone.now())
