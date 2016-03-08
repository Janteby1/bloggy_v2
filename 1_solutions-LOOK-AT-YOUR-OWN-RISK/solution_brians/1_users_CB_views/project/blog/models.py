from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=4000)
    slug = models.SlugField(max_length=40)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    user = models.ForeignKey(
        User,
        null = True,
        default = None,
        on_delete = models.SET_DEFAULT,
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.updated_at = timezone.now()
        if not self.id:
            self.created_at = timezone.now()
        super(Post, self).save(*args, **kwargs)
        

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    user = models.ForeignKey(
        User,
        null = True,
        default = None,
        on_delete = models.SET_DEFAULT,
    )
    post = models.ForeignKey(
        Post,
        null = True,
        default = None,
        on_delete = models.CASCADE,
    )


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username