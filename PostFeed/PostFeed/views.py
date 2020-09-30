from django.http import HttpResponse

from PostFeed.models import Post


def MainPage(request):
    tom = Post.objects.create(name="C#",
                              text="C# is better than python;",
                              author="BugBoyz",
                              date="1.10",
                              tags="important")
    # render
    return HttpResponse("Main Page!")
