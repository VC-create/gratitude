from django.urls import path
from pages import views 

#this sets up the urls for our pages app
urlpatterns = [
    #empty quotes show that the user hasn't typed in extra subdomains and want to go to our plain website
    #views.home refers to the function we made in views
    #name="home" shows how we can refer to it later
    path("", views.home, name="home")
]