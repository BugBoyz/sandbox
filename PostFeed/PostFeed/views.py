from django.shortcuts import render, redirect
from PostFeed.models import Post
from django.views.decorators.csrf import csrf_exempt
import datetime
from .forms import PostForm


def MainPage(request):
    data = Post.objects.all()
    return render(request, "mainPage.html", {"context": data})


def AddPost(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, "addPost.html", {"form": form})

    elif request.method == 'POST':
        Post.objects.create(
            name=request.POST['name'],
            author=request.POST['author'],
            text=request.POST['text'],
            tags=request.POST['tags'],
            date=datetime.datetime.now()
        )

        return redirect('/../')


def DeletePost(request, postID):
    Post.objects.get(id=postID).delete()

    return redirect('/../')


def ShowPost(request, postID):
    post = Post.objects.get(id=postID)

    return render(request, "ShowPost.html", {"post":post})