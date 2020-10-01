from django.http import HttpResponse
from django.shortcuts import render
from PostFeed.models import Post


def MainPage(request):
    data = Post.objects.all()
    return render(request, "mainPage.html", {"context":data})
