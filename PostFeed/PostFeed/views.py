from django.shortcuts import render, redirect
from PostFeed.models import Post
from django.views.decorators.csrf import csrf_exempt
import datetime

def MainPage(request):
    data = Post.objects.all()
    return render(request, "mainPage.html", {"context": data})


def AddPost(request):
    return render(request, "addPost.html")


@csrf_exempt
def AddPostLogic(request):
    Post.objects.create(
        name=request.POST['name'],
        author=request.POST['author'],
        text=request.POST['text'],
        tags=request.POST['tags'],
        date=datetime.datetime.now()
    )

    return redirect('/../')