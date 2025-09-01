from django.contrib import admin
from .models import Post

# Register your models here.

#now we're saying add the model to the admin site so that whenver we log into the site, we can edit, change, add posts without having to write a whole new code for it
admin.site.register(Post)
