import datetime
import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect

from PostFeed.models import Post, User
from .forms import PostForm, AuthForm, SearchString


def MainPage(request):

    if request.method == "POST":
        searchWord = request.POST["searchWord"]

        filtered_name = Post.objects.filter(
            name__contains=searchWord,
        )

        filtered_author = Post.objects.filter(
            author__contains=searchWord
        )

        filtered_tags = Post.objects.filter(
            tags__contains=searchWord
        )

        context = filtered_name.union(
            filtered_author.union(
                filtered_tags
            )
        )

        if len(context) == 0 or context is None:
            context = ""

        return render(request, "mainPage.html",
                      {'context': context,
                       'filtered': True,
                       'authorized': request.session['authorized'],
                       'username': request.session['username'],
                       "form": SearchString()})

    try:
        data = Post.objects.all()
        if request.session['authorized'] == True:
            return render(request, "mainPage.html",
                          {"context": data,
                           'authorized': True,
                           'username': request.session['username'],
                           "filtered": False,
                           "form": SearchString()})

        else:
            return render(request, "mainPage.html",
                          {'context': data,
                           'authorized': False,
                           "filtered": False,
                           "form": SearchString()})

    except:
        data = Post.objects.all()
        return render(request, "mainPage.html",
                      {'context': data,
                       'authorized': False,
                       "filtered": False,
                       "form": SearchString()})


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
    try:
        post = Post.objects.get(id=postID)

        if request.session['authorized'] == True \
                and str(request.session['username']) == str(post.author):
            post.delete()

        else:
            return HttpResponse("<h1 align=\"center\">А хуй тебе, гнида хитрожопая!</h1>")
    except:
        return HttpResponse("<h1 align=\"center\">А хуй тебе, гнида хитрожопая!</h1>")

    return redirect('/../')


def ShowPost(request, postID):
    post = Post.objects.get(id=postID)

    try:
        if request.session['authorized'] == True:
            return render(request, "ShowPost.html", {"post": post,
                                                     'authorized': True,
                                                     'username': request.session['username']})
        else:
            return render(request, "ShowPost.html", {"post": post,
                                                     'authorized': False})
    except:
        return render(request, "ShowPost.html", {"post": post,
                                                 'authorized': False})


def Authorize(request):
    if request.method == 'GET':
        form = AuthForm()

        return render(request, "Auth.html", {"form": form, "exception": False})

    elif request.method == 'POST':
        try:
            User.objects.get(
                username=request.POST['username'],
                password=hashlib.md5(str(request.POST['password']).encode()).hexdigest())
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


