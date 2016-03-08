# Userful Blog + Class Based Views

##### Description

* Over the weekend we built out a userless blog crud application
* Todays assignment is to copy that project into this repo and add on to it
	* If you feel like you want more practice try replicating what you did over the weekend from scratch. 
* Alongside the extra Model you will also need to refactor your function based views to class based views.
* From now on we will be using Class Based Views

##### Objectives

* The blog will allow multiple users to sign up, log in, and write posts. 
* An unauthenticated user should only be able to view posts but cannot write any

##### The Main Page

* The main page should display all the posts
* There should be an "author" or "user" that appears next to each post 
* Order the post by the most recent
* Each title should link to that posts detailed view

***Bonus***

* How would you let the user change the order? 
* Maybe change it by title?
* Maybe change it by author?

##### The User Page

* If a user visit their page they should see a list of all their own posts
* You can use the same format you did in the main page

##### Editing

* A user should be able to edit their own posts but not the posts of others

##### Comments

* A user should be able to post comments to any post
* A post should always show the content along with the author
* A post in detailed view should always display the comments below itself

##### BONUS: Nested Comments

* Add comments to comments!
* How can a user reply to a comment? 
* Then have the reply appear below that comment
* The best way to do this is with a [Generic Relation](https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/#generic-relations) in comments. For reference, this is sometimes called a Polymorphic Association.
* Make sure that you edit the css so that a nested comment's div is clearly indented below its parent.

## NOTES

* You may feel like you're already halfway done with this application because we did some of it over the weekend
* DO NOT just start coding
* Write out your user stories
	* What can these users do
	* What should they not be allowed to do
	* You were given some user stories up top but are there any more you can think of?
* Write out your pseudo code
	* What will your Models look like
	* What will your class based views look like
* Draw out your wireframe
	* Since we're getting into users and allowing them to post and comment, what will that user experience look like? 
* WORK TOGETHER!!!
	* Work together if not for the whole time at least for the planning phase.
	* Utilize Trello and Github to plan your assignment
	* Pair program. One person drives and the other navigates

***We're a team, lets do this together so we can kick ass in phase 3***
