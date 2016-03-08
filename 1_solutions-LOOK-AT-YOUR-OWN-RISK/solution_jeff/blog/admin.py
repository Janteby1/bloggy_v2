from django.contrib import admin

# import your model
from blog.models import UserProfile, Post

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)