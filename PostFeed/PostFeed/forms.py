from django import forms


class PostForm(forms.Form):
    name = forms.CharField(max_length=30, label='Название')
    text = forms.Field(label='Статья', widget=forms.Textarea)
    tags = forms.CharField(max_length=50, label='Тэги')


class AuthForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
