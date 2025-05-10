from django.db import models
from django.urls import reverse
from django.utils import timezone
from account.models import User
from django.utils.html import format_html
from extensions.utils import jalali_converter
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


#My managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)

# Create your models here.

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس آی پی")

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL, related_name="children", verbose_name="subscription")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True, verbose_name="show this?")
    position = models.IntegerField()
    class Meta:
        verbose_name="Category"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title
    objects = CategoryManager()

class Article(models.Model):
    STATUS_CHOICES = (
        ("d", "Draft"),
        ("p", "Published"),
        ("i", "investigation"),
        ("b", "back")
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles', verbose_name='author')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ManyToManyField(Category, related_name="articles")
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    is_special = models.BooleanField(default=False, verbose_name= "مقاله ویژه")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through="ArticleHit", blank=True, related_name="hits", verbose_name="بازدید ها")

    class Meta:
        verbose_name="Article"

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description = 'pulish date'

    def thumbnail_tag(self):
        return format_html("<img width=100 height=70 src='{}' style='border-radius:5px'>".format(self.thumbnail.url))
    thumbnail_tag.short_description = "picture"

    def get_absolute_url(self):
        return reverse("account:home")    
    def category_published(self):
        return self.category.filter(status=True)
    objects = ArticleManager()
    
    def category_to_str(self):
        return ", ".join([category.title for category in self.category.active()])
    category_to_str.short_description = 'category'
    
class ArticleHit(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
