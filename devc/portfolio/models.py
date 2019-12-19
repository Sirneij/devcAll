from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.urls import reverse
# Create your models here.


class Introduction(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="portfolio_user")
	title = models.CharField(max_length=500)
	passion = models.TextField(blank=True, null=True)
	def __str__(self):
		return 'Introduction by {} with title {}'.format(self.user.username, self.title)

class Work(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="work_user")
	commencement = models.DateField(auto_now=False, auto_now_add=False)
	end = models.DateField(auto_now=False, auto_now_add=False)
	company_name = models.CharField(max_length=500)
	position = models.CharField(max_length=500)
	description = RichTextField(config_name='awesome_ckeditor')
	def __str__(self):
		return '{} worked at {}'.format(self.user.username, self.company_name)

	def get_markdown(self):
		description = self.description
		return mark_safe(description)
	def get_absolute_url(self):
		return reverse('portfolio:portfolio_index',args=[self.user])

class Education(models.Model):
	DEGREE_CHOICES = ( 
        ('high school certificate', 'High School Certificate'), 
        ('diploma', 'Diploma'), 
        ('bachelor', 'Bachelor'),
        ('masters', 'MAsters'),
        ('phd.', 'PhD.'),
        ('self-taught', 'Self-Taught'), 
    ) 
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education_user")
	commencement = models.DateField(auto_now=False, auto_now_add=False)
	end = models.DateField(auto_now=False, auto_now_add=False)
	school_name = models.CharField(max_length=500)
	degree_type = models.CharField(max_length=100,  choices=DEGREE_CHOICES, default='high school certificate') 
	description = RichTextField(config_name='awesome_ckeditor')
	def __str__(self):
		return '{} schooled at {}'.format(self.user.username, self.school_name)

	def get_markdown(self):
		description = self.description
		return mark_safe(description)

	def get_absolute_url(self):
		return reverse('portfolio:portfolio_index',args=[self.user])

class Project(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects_user")
	title = models.CharField(max_length=500)
	category = models.TextField()
	caption = RichTextField(config_name='awesome_ckeditor')
	project_pic = models.ImageField(upload_to='projects_pics')
	def __str__(self):
		return '{} on {}'.format(self.title, self.category)

	def get_markdown(self):
		caption = self.caption
		return mark_safe(caption)

class Service(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_user")
	title = models.CharField(max_length=500)
	description = RichTextField(config_name='awesome_ckeditor')
	
	def __str__(self):
		return '{} on {}'.format(self.intro, self.title)

	def get_markdown(self):
		description = self.description
		return mark_safe(description)
	def get_absolute_url(self):
		return reverse('portfolio:portfolio_index',args=[self.user])

class Testimonial(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="testimonial_user", default=1)
	recommender_name = models.TextField()
	recommender_office = models.CharField(max_length=500)
	content = RichTextField(config_name='awesome_ckeditor')
	recommender_pic = models.ImageField(upload_to="recommenders_pics", default="user-01.jpg")

	def __str__(self):
		return "Recommended by {} a {}".format(self.recommender_name, self.recommender_office)

	def get_markdown(self):
		content = self.content
		return mark_safe(content)
	def get_absolute_url(self):
		return reverse('portfolio:portfolio_index',args=[self.user])