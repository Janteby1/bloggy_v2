# MOAR DJANGO FEATURES

### Learning Objectives
***Students will be able to...***

* Use Class Based Views over Function Based Views
* Use `sessions` to store data

---
### Context

* Continuing to become Full Stack Developers

---
### Lesson

##### Part 1 - Static Files

* Static File notes have been in your parking lot but we'll go over them briefly
* `Static Files` are your
	* images
	* CSS stylesheets
	* JavaScript files
* Here are the Django docs for how to set them up [static folder documentation](https://docs.djangoproject.com/en/1.8/howto/static-files/)
* Your `settings.py` file will have to be changed to include the static files
* Put the following code at the very bottom of your `settings.py` file under `STATIC_URL`

```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"), 
    '/var/www/static/',
)
```
* os.path.join and Base_dir allow our application to be more dynamic with compatibility between different operating systems. 
	* A path on Linux may be different than Mac
* We are telling django to combine your static folder with the base directory
* Now we can incorporate our css stylesheets into our base html

***STEPS***

* Make a folder called `static` inside your project.
* Make a `style.css` file inside that `static` folder
* Open the css file and put in some CSS. `h1{color:red;}`
* Go into your base.html file and put the following

```
{% load staticfiles %}

<!DOCTYPE html>
<html lang="en">
<head>
	<link rel="stylesheet" href="{% static "css/base.css" %}">
	<meta charset="UTF-8">
	<title>{% block head_title %}TRY DJ 1.9{% endblock head_title%}</title>
</head>
```
* Now your h1 tags should appear red


##### Part 2 - Class Based Views

* Lets talk about how you may begin to write/refactor your code to incorporate Class Based Views

***urls.py***

* Your urls.py file will not change much
* You will still need to import your views 

```
from .views import (
	Post_Home,
	Post_Detail
)
```
* Notice they are capitalized, we are importing classes now\
	* The first letter when defining a class is Capitalized
* The url patters will follow the same format
	* url("regex url endpoint", view targeted, name="template value")

```
urlpatterns = [
	url(r'^$', Posts_List.as_view(), name='list'),
	url(r'^(?P<id>\d+)/$', Posts_Detail.as_view(), name='detail'),
]
```
* Notice the `as_view()` method here. Since we are dealing with classes instead of functions, the `as_view()` is a built in method which will allow us to call the classes when the endpoint is hit

***views.py***

* You will need to import views from django

```
from django.views.generic import View
```
* The most basic view, our home view, will look very similar to the function based way of doing things

```
class Posts_List(View):
	def get(self, req):
		whiskey_list = Post.objects.all()
		context = {
			"whiskey_list": whiskey_list,
		}
		return render(req, "posts/list.html", context)
```
* Our detail view will look a little bit different

```
class Posts_Detail(View):

	def get(self, req, **kwargs):
		whiskey = get_object_or_404(Post, id=kwargs['id'])
		context = {
			"whiskey":whiskey
		}
		return render(req, "posts/detail.html", context)
```

***FIFO TIME***

* For your assignment tonight how might you incorporate these forms into these new class based views.


##### Part 3 - Two Apps

* Very brief discussion
* Using multiple apps is just a matter of importing them
* We've done this already by importing models from `forms.py`
* Now we'll just be targeting an outside application
* The below example will be in your `project/posts/views.py`

```
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from Users.models import User

def user_post(request):
	user = User.objects.get(email=email)
```


##### Part 4 - User Sessions