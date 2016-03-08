from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from users.forms import LoginForm
from users.models import User

# Create your views here.

class Login(View):
    template = "users/login.html"

    def get(self, request):
        context = {
            "login_form": LoginForm(),        
        }
        return render(request, self.template, context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.filter(
                username=username, 
                password=password
        ).first()
        
        if user:
            request.session['username'] = user.username
            return redirect("blog:index")
        elif login_form.is_valid():
            #send 'user not found' message
            login_form = LoginForm()
        
        context = {
            "login_form": login_form,        
        }
        return render(request, self.template, context)

class Logout(View):
    def get(self, request):
        del request.session['username']
        return redirect("blog:index")

