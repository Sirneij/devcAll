from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.conf import settings
from ckeditor.fields import RichTextField
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_pics = models.ImageField(default='default.png', upload_to='users/%Y/%m/%d/')
    bio = RichTextField()
    phone_regex = RegexValidator(regex=r'^\+\d*$', message="Phone number must be entered in the format: '+999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True)
    twitter_url = models.URLField(max_length=1000, null=True, blank=True)
    facebook_url = models.URLField(max_length=1000, null=True, blank=True)
    linkedin_url = models.URLField(max_length=1000, null=True, blank=True)
    github_url = models.URLField(max_length=1000, null=True, blank=True)
    codepen_url = models.URLField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    def get_account_absolute_url(self):
        return reverse('account:edit',args=[self.user.username])

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_pics.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pics.path)
