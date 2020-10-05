import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from PostFeed.models import Post, User
from .forms import PostForm, AuthForm, SearchString


def MainPage(request):
    data = Post.objects.all()

    try:
        if request.session['authorized'] == True:
            return render(request, "mainPage.html",
                          {"context": data,
                           'authorized': True,
                           'username': request.session['username'],
                           "filtered": False})

        else:
            return render(request, "mainPage.html",
                          {'context': data,
                           'authorized': False,
                           "filtered": False})

    except:
        return render(request, "mainPage.html",
                      {'context': data,
                       'authorized': False,
                       "filtered": False})


def AddPost(request):
    if request.session['authorized'] == True:
        if request.method == 'GET':
            form = PostForm()
            return render(request, "addPost.html", {"form": form})

        elif request.method == 'POST':
            Post.objects.create(
                name=request.POST['name'],
                author=request.session['username'],
                text=request.POST['text'],
                tags=request.POST['tags'],
                date=datetime.datetime.now()
            )

            return redirect('/../')
    else:
        return HttpResponse("<h1 align=\"center\">А хуй тебе, гнида хитрожопая!</h1>")


def DeletePost(request, postID):
    Post.objects.get(id=postID).delete()

    return redirect('/../')


def ShowPost(request, postID):
    post = Post.objects.get(id=postID)

    return render(request, "ShowPost.html", {"post": post})


def Authorize(request):
    if request.method == 'GET':
        form = AuthForm()

        return render(request, "Auth.html", {"form": form, "exception": False})

    elif request.method == 'POST':
        try:
            User.objects.get(
                username=request.POST['username'],
                password=request.POST['password'])
            request.session['username'] = request.POST['username']
            request.session['authorized'] = True

            return redirect('/../')

        except:
            form = AuthForm()
            return render(request, "Auth.html", {'form': form, 'exception': True})


def SignOut(request):
    request.session['authorized'] = False
    request.session['username'] = ''

    return redirect('/../')


def Search(request):
    if request.method == 'GET':
        form = SearchString()
        return render(request, "searchPage.html", {"form": form, "filtered": False})

    else:

        searchCategory = request.POST["searchCategory"]
        searchWord = request.POST["searchWord"]

        filtered = Post.objects.filter(
            name__contains=searchWord,
        )

        if len(filtered) == 0:
            filtered = ""

        return render(request, "mainPage.html", {"context": filtered,
                                                 "filtered": True,
                                                 'authorized': request.session['authorized'],
                                                 'username': request.session['username']})
