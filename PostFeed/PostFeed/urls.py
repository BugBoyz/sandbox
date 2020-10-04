"""PostFeed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from PostFeed import views

urlpatterns = [
    path('addPost/', views.AddPost),
    path('', views.MainPage),
    path('deletePost/<int:postID>', views.DeletePost),
    path('Post/<int:postID>', views.ShowPost)
    #re_path(r'^main', views.)
]
