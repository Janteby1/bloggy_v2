from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, UpdateView, CreateView, DeleteView
from blog.forms import UserForm, UserProfileForm, PostForm
from blog.models import Post
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class User_Register(View):
    template = "registration.html"

    def get(self, request):
        if request.user.is_authenticated():
            return render(request, "index.html", {})
        user_form = UserForm()
        profile_form = UserProfileForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, self.template, context)

    def post(self, request):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            #Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            profile = profile_form.save(commit=False)
            profile.user = user
            # Now we save the UserProfile model instance.
            profile.save()
            return redirect('/')
        else:
            context = {
                'user_form': user_form,
                'profile_form': profile_form
            }
            return render(request, self.template, context)

class User_Login(View):
    template = "login.html"

    def post(self, request):
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
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
                return redirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    def get(self, request):
        if request.user.is_authenticated():
            return render(request, "index.html", {})
        return render(request, 'login.html', {})


class Post_List(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
    # or
    # replace model with
    # queryset = Book.objects.order_by('-publication_date')


class Post_Detail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'detail.html'


class Update_Post(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "create.html"
    success_url = "/blog/"


class Create_Post(CreateView):
    form_class = PostForm
    template_name = "create.html"
    success_url = '/blog/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super(Create_Post, self).form_valid(form)

    #need to customize login url in settings
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(Create_Post, self).get(request, *args, **kwargs)


class Delete_Post(DeleteView):
    model = Post
    success_url = '/blog/'
    template_name = 'delete.html'

    #need to customize login url in settings
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        return super(Delete_Post, self).get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            return HttpResponse("thats not ur post u can't delete it.")
        return super(Delete_Post, self).delete(request, *args, **kwargs)



# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return redirect('/')
