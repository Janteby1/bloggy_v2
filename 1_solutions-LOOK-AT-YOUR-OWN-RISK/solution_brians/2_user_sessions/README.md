# User Login with Sessions

### Description

* Lets apply [sessions](https://docs.djangoproject.com/en/1.8/topics/http/sessions/) to our new blog
* Sessions allow us to store data between requests on either the client or server side. 
* Remember HTTP is a stateless protocol. This means it does not save any data
* With sessions we can prevent the hassle of making users log in every time they went to a new page

### Objectives!!!

---

##### Start

* Start a brand new project in a new virtual env
* Bring in your users app here
* Make the settings and migration edits
* Now add this line to the `settings.py` file 

```
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
```
* This will tell Django to use cookies for session data:

##### Routes

* Make two different Post Routes
	* One route will handle user registration
	* Other route will handle user log in
* Templates
	* You can make two separate templates and link them
	* How might you put a form on the same template and have that work? 
* When a user is finished either registering or logging in they should be redirected back to a "User Welcome" Page

##### Password Hashing

* Before we use cookies we want to make sure our users data is secure in our DB
* Until now we've been storing our passwords as strings in the database.
* This is definitely NOT how you want it to be done.
* Take a look at this bit of the [Django docs on password management](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#module-django.contrib.auth.hashers)

***So what the hell does this mean?***

* Password hashing means to take in user input for a password and run it through an algorithm where the output results in an extremely long string of seemingly random characters and numbers
* The idea is when a user enters their password, it will go through the process of this algorithm and if the output matches the hash in the database the user is verified
* We will be using Bcrypt to hash our passwords. 
	* Take a look at [BCrypt with Django](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#using-bcrypt-with-django). 
	* For more information about [Bcrypt here is their wiki](https://en.wikipedia.org/wiki/Bcrypt) 	

***TESTING***

* Follow the instructors in the [BCrypt with Django Docs](https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#using-bcrypt-with-django). 
* Once installed open up the django shell `py manage.py shell`
* Print out a users password. 
* SECURITY!!!

***SIDE NOTE***

* If you lost your password and a company emails your exact password back, instead of verification/ask for a new one, then they are storing your password as is in their database. It's completely insecure

***YOUR APP***

* Okay now that you have it installed we can go back to our crud app
* If the password does not match re-render the login page
* If the password does is verified send them to the "User Welcome" page


##### Sessions Login

* Okay sorry for the long detour into the realm of password security
* Let's get back to business and talk about sessions
* We want to store a session key.
* Sessions are a part of the request object. You can see the keys by printing 

```
request.session.keys()
```
* You can make a new session variable by typing

```
request.session['your_key'] = value
```
* If a user is verified during log in, store their session key, along with their id as a value.

```
def user_login(request):
    username, password = request.POST['username'], request.POST['password']
    # Check if form values are valid
        # if valid:
            # try to query DB for user
                #if the user exists
                    #verify passwords
                        #if username and passwords match:
                            # SET session key her
                            # return redirect to user page
        # else return redirect with errors
```
* Edit the welcome page
	* You no longer want to use values found in the URL or view function argument
	* Instead you will utilize the verified user_id in the stored session to load that user object from the database
	* Remember, the user_id that you will be using will come from storing that session. This means they are logged in. If they are NOT logged in (no session value) then they should go back to the login page
		* check out `session.get` 
		* This method will help with that issue 

```
def welcome_page(request):
    #if session with user_is found;
        # query user
        # render user page with retrieved user information
    #else:
        # send them to login page
```

##### Loggin Out

* Make a logout page that clears the session when the user hits the route
* Redirect to the main page
* HINT: Django has a built in function for this

##### BONUS: EXPIRATION

* How might you add an expiration to the session? 
* If the user is idle for too long how can you automatically log them off?
* Is there a way to set the time to our own preference?
* If so then you could set the time to a few seconds for testing purposes to see if it works.
