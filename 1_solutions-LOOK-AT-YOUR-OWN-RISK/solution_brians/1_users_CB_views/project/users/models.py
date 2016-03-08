from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(
        max_length = 20,
        unique = True,
    )
    password = models.CharField(max_length=20)
    email = models.CharField(
        max_length = 40,
        unique = True,
    )
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()


    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        if not self.id:
            self.created_at = timezone.now()
        super(User, self).save(*args, **kwargs)
