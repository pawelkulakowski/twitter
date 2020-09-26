from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


def user_directory_path(instance, filename):
    # user_123/avatar.jpg
    return "user_{0}/{1}".format(instance.id, filename)
    #return f"{uuid.uuid4()}{ext}"

class TwitterUser(AbstractUser):
    email = models.EmailField(_("email address"), blank=True, unique=True)
    avatar = models.ImageField(
        upload_to=user_directory_path,
        height_field="avatar_height",
        width_field="avatar_width",
        null=True,
        blank=True
    )
    avatar_height = models.SmallIntegerField(null=True, editable=False)
    avatar_width = models.SmallIntegerField(null=True, editable=False)