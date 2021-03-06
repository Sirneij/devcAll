from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.db.models.signals import pre_save
from PIL import Image
from taggit.managers import TaggableManager
from .utils import get_read_time
from django.utils.safestring import mark_safe
#from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.TextField(max_length=1000000)
    slug = models.SlugField(max_length=10000000, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=10000000)
    slug = models.SlugField(max_length=10000000, unique_for_date='publish')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    image = models.ImageField(upload_to='posts_pics', default='logo.svg')
    body = RichTextUploadingField()
    publish = models.DateTimeField(default=timezone.now)
    # models.TimeField(null=True, blank=True) #as sume minutes
    read_time = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=100,  choices=STATUS_CHOICES, default='draft')
    # ovation = models.ManyToManyField(User, blank=True, related_name="ovation")
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.
    #hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = TaggableManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def get_next_post(self):
        return self.get_next_by_created()

    def get_previous_post(self):
        return self.get_previous_by_created()

    def get_markdown(self):
        body = self.body
        return mark_safe(body)

    # def total_ovations(self):
    #     return self.ovation.count()

    # @property
    # def comments(self):
    #     instance = self
    #     qs = Comment.objects.filter_by_instance(instance)
    #     return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.image.path)
        width = 883
        height = 391
        if img.width > width or img.height > height:
            output_size = (width, height)
            img.thumbnail(output_size)
            img.save(self.image.path)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.body:
        html_string = instance.get_markdown()
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=Post)

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     reply = models.ForeignKey('Comment', null=True, on_delete=models.CASCADE, related_name='replies')
#     body = RichTextUploadingField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ('created',)

#     def __str__(self):
#         return 'Comment by {} on {}'.format(self.author.username, self.post.title)

#     def get_markdown(self):
#         body = self.body
#         return mark_safe(body)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    path = ArrayField(models.IntegerField(), blank=True, editable=False)
    depth = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author.username, self.post.title)

    def get_markdown(self):
        content = self.content
        return mark_safe(content)


class SearchTerm(models.Model):
    """Model definition for SearchTerm."""

    query = models.CharField(max_length=2000)
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             null=True, on_delete=models.SET_NULL)
    tracking_id = models.CharField(max_length=50, default='')

    class Meta:
        """Meta definition for SearchTerm."""

        verbose_name = 'SearchTerm'
        verbose_name_plural = 'SearchTerms'

    def __str__(self):
        """Unicode representation of SearchTerm."""
        return self.query

    def get_absolute_url(self):
        """Return absolute url for SearchTerm."""
        return ('')
