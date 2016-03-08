from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm, UserProfileForm, PostForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import pudb
from django.contrib.auth.decorators import login_required #fancy decorator
from .models import UserProfile, Post
from django.contrib.auth.models import User


# Create your views here.
class Index(View):
    def get(self, request):
        context = {}
        if request.user.is_authenticated(): # check to see if someone is already logged in 
            username = request.user.username
            # username = User.objects.get(username=username)
            message = ("Hello, " + username + " You are logged in")
            context = {
                'message': message,
            }
            # return render(request, "blog/index.html", context)

        # this line gets all the todos that we have in the db
        posts = Post.objects.all().order_by('-updated_at')
        # creates them into a context dict
        context["posts"]=posts
        # context = {
        #     'posts': posts,
        # }
        # send them all to the template
        return render(request, "blog/index.html", context)

class User_Register(View):
    # pu.db
	# link to our tamplate page
    template = "blog/register.html"

    def get(self, request):
        user_form = UserForm()
        profile_form = UserProfileForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        # using self is a fancy way to give a variable name to the template ...?
        return render(request, self.template, context)

    def post(self, request):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            profile = profile_form.save(commit=False)
            profile.user =user
            print (profile.user)
            # Now we save the UserProfile model instance.
            profile.save()
            # return render(request, "blog/index.html", {})
            return redirect("posts:index")
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            return render(request, self.template, context)

class User_Login(View):
    template = "blog/login.html"

    def post(self, request):
        # Gather the username and password provided by the user.
        # This information is obtained from the login HTML form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                # username = request.user.username
                # message = ("Hello, " + username + " You are signed in")
                # context = {
                #     'message': message,
                # }
                # return render(request, "blog/index.html", context)
                return redirect("posts:index")

            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    def get(self, request):
        # if the user is already signed in 
        if request.user.is_authenticated():
            # username = request.user.username
            # # username = User.objects.get(username=username)
            # message = ("Hello, " + username + " You are already signed in")
            # context = {
            #     'message': message,
            # }
            return redirect("posts:index")
        return render(request, self.template, {})

class User_Logout(View):
    # Use the login_required() decorator to ensure only those logged in can access the view.
    # @login_required
    def get(self, request):
        # Since we know the user is logged in, we can now just log them out.
        logout(request)
        # Take the user back to the homepage.
        return redirect("posts:index")

class Create_Post(View):

    def get(self, request):
        form = PostForm()
        context = {
            "PostForm": form }
        return render (request, "blog/create.html", context)




    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        form = PostForm(data=request.POST)

        if form.is_valid():
            # need to save the username the post is attached to
            user = request.user
            print (user) 
            post = form.save(commit=False)
            post.user = user 
            post.save()
            return redirect("posts:index")

        else:
            context = {
                "PostForm": form,
            }
            return render(request, 'blog/create.html', context)
    # else:
    #     return HttpResponseNotAllowed(['GET', 'POST'])


class Edit_Post(View):
    # def edit(request, post_slug):   
    def get(self, request, post_slug=None):
        post = Post.objects.get(slug=post_slug)
        form = PostForm(instance=post)
        context = {
            "post": post,
            "EditForm": form,
        }
        return render(request, "blog/edit.html", context)

    def post(self, request, post_slug=None):
        post = Post.objects.get(slug=post_slug)
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:index")
        else:
            context = {
                "post": post,
                "EditForm": form,
            }
            return render(request, 'blog/edit.html', context)
    # else:
    #     return HttpResponseNotAllowed(['GET', 'POST'])

class Delete_Post(View):
    def post(self, request, post_slug=None):
        post = Post.objects.get(slug=post_slug)
        post.show = False
        post.save()
        return redirect('posts:index')



