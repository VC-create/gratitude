from django.shortcuts import render
#need to import the model we made
#the . means it's a page in our directory
from .models import Post

# Create your views here.

#when you use the internet, you're sending requests to the website, it has user name, time, what they're doing
def home(request):
    #collects all the posts we've written
    posts = Post.objects.all()

    #now we want to pass along our posts to the html
    #context is a dictionary, it has a title and stuff in it, where we can refer to it by a text name
    context = {
        "posts": posts
    }
    #render returns all the info given to the web browser - html, css, etc
    return render(request, "home.html", context)

#pk means primary key, to only run the function with the pk in the url
def detail(request, pk):
    #get one specific post
    #pk=pk means that the pk of the post is the pk that we're looking for
    this_post = Post.objects.get(pk=pk)
    #in detail.html we reference post, so we need to make it post here, so that it shows what the post says
    #context is what we pass to the template, so when detail.html says post, pass it this_post
    #it doesn't have to be post, it could be any word, but whatever is in the quotes has to match what's in detail.html
    context = {
        "post": this_post
    }
    return render(request, "detail.html", context)


