from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404,
)
from django.views.generic import View
from blog.models import *
from blog.forms import *
from django.contrib.auth.models import User


class Index(View):
    def get(self, request):
        username = request.session.get('username', None)
        all_posts = Post.objects.all()
        context = {
            "all_posts": all_posts,      
            "username": username,
        }
        return render(request, "blog/index.html", context)


class User_Index(View):
    def get(self, request):
        username = request.session.get('username', None)
        user = User.objects.get(username=username)
        user_posts = Post.objects.filter(user=user.id)
        context = {
            "all_posts": user_posts,
            "username": username,
        }
        return render(request, "blog/user.html", context)


class Post_Add(View):
    template = "blog/add.html"

    def get(self, request):
        username = request.session.get('username', None)
        if not username:
            return redirect("blog:index")
        context = {
            "new_post_form": PostForm(),
            "username": username,
        }
        return render(request, self.template, context)

    def post(self, request):
        username = request.session.get('username', None)
        user = User.objects.get(username=username)
        new_post_form = PostForm(request.POST)
        user = User.objects.get()
        if new_post_form.is_valid():
            new_post_form.save(user)
            return redirect("blog:index")
        context = {
            "new_post_form": new_post_form,
        }
        return render(request, self.template, context)


class Post_Edit(View):
    template = "blog/edit.html"

    def get(self, request, id):
        target_post = get_object_or_404(Post, id=id)
        edit_post_form = PostForm(instance = target_post)
        context = {
            "post": target_post,
            "edit_post_form": edit_post_form,
        }
        return render(request, self.template, context)

    def post(self, request, id):
        target_post = get_object_or_404(Post, id=id)
        edit_post_form = PostForm(request.POST, instance = target_post)
        if edit_post_form.is_valid():
            edit_post_form.save()
            return redirect("blog:index")
        context = {
            "post": target_post,
            "edit_post_form": edit_post_form,
        }
        return render(request, self.template, context)
        

class Post_Delete(View):
    def post(self, request, id):
        target_post = get_object_or_404(Post, id=id)
        target_post.delete() 
        return redirect("blog:index")


class Post_Details(View):
    template = "blog/details.html"

    def get(self, request, id):
        post = get_object_or_404(Post, id=id)
        context = {
            "post": post,       
        }
        return render(request, self.template, context)
