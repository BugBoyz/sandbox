from django import forms


class PostForm(forms.Form):
    name = forms.CharField(max_length=30, label='Название')
    author = forms.CharField(max_length=25, label='Автор')
    text = forms.Field(label='Статья', widget=forms.Textarea)
    tags = forms.CharField(max_length=50, label='Тэги')