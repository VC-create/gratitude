from django.shortcuts import render

# Create your views here.

#when you use the internet, you're sending requests to the website, it has user name, time, what they're doing
def home(request):
    #render returns all the info given to the web browser - html, css, etc
    return render(request, "home.html", {})

