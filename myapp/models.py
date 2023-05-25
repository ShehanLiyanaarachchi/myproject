from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add any additional fields or modifications to the User model

    class Meta:
        swappable = 'AUTH_USER_MODEL'

User._meta.get_field('groups').remote_field.related_name = 'myapp_user_set'
User._meta.get_field('user_permissions').remote_field.related_name = 'myapp_user_set'