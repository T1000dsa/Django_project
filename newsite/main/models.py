from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
# Create your models here.
# from django.db.models import Q, F, Avg, Sum, Count
# from main.models import Helmet, Worker, TagModel, Category
# python manage.py migrate main {000#}

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Worker.Status.Published)
    
class Worker(models.Model):
    class Status(models.IntegerChoices):
        Draft = 0, 'Unpublished'
        Published = 1, 'Published'

    title = models.CharField(max_length=256, verbose_name='Title')
    slug = models.SlugField(max_length=256, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Content')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x:(bool(x[0]), x[1]),Status.choices)), default=Status.Draft)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT,null=True,blank=True) # cat.worker_set
    tags = models.ManyToManyField('TagModel', blank=True, related_name='tags', null=True)
    helmet = models.OneToOneField('Helmet', on_delete=models.SET_NULL, blank=True, related_name='worhel',null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', default=None, blank=True, null=True, verbose_name='Photo')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,default=None, blank=True,null=True, related_name='author_worker')

    objects = models.Manager()
    published = PublishedManager()


    def get_absolute_url(self):
        return reverse('show', kwargs={'post_slug':self.slug})
    
    def get_pk(self):
        return reverse('update', kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Best team ever'
        verbose_name_plural = 'Best team ever'


class Category(models.Model):

    name = models.CharField(max_length=64, db_index=True)
    slug = models.SlugField(max_length=256, unique=True, db_index=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug':self.slug})
    
class TagModel(models.Model):
    tag = models.CharField(max_length=96, db_index=True)
    slug = models.SlugField(max_length=128, unique=True, db_index=True)
    def __str__(self):
        return self.tag
    
    def get_absolute_url(self):
        return reverse('show_tag', kwargs={'tag_slug':self.slug})
    
    
class Helmet(models.Model):
    helmet_name = models.CharField(null=True, default='Helmet', max_length=64)
    usage_count = models.IntegerField(default=0, blank=True)

class UploadFiles(models.Model):
    file = models.FileField(upload_to='photos_other/%Y/%m/%d')