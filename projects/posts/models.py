from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone #make sure to set the timezone 

# Create your models here.
class UserProfile(models.Model):
	# this line links UserProfile to a user model instance
	user = models.OneToOneField(User)
	# here we can add aditional attributes 
	m_name = models.CharField(max_length=40)

	'''
	Includes these attributes:
	Username, Password, Email address, firstname, surname
	'''

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=4000)
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    show = models.BooleanField(default=True)
    user = models.ForeignKey(User) # adds a FK

    # this is a custom save method
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.updated_at = timezone.now()
        # self.user = user
        if not self.id:
            self.created_at = timezone.now()
        super(Post, self).save(*args, **kwargs)



