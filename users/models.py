from django.db import models
from django.contrib.auth.models import User
from PIL import Image

MAX_PROFILE_PIC_SIZE = 300


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > MAX_PROFILE_PIC_SIZE or img.width > MAX_PROFILE_PIC_SIZE:
            output_size = (MAX_PROFILE_PIC_SIZE,MAX_PROFILE_PIC_SIZE)
            img.thumbnail(output_size)
            img.save(self.image.path)
