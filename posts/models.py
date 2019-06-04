from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Categories(models.Model):
    CATEGORIES_CHOICES = (
        ('news', 'Новости'),
        ('economics', 'Экономика'),
        ('science', 'Наука'),
        ('tech', 'Техника'),
        ('it', 'IT'),
        ('none', 'Без категории')

    )

    title = models.CharField(
        max_length=20,
        choices=CATEGORIES_CHOICES,
        default='none'
    )

    slug = models.SlugField(
        max_length=20
    )

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликован'),
    )

    title = models.CharField(
        max_length=250
    )
    slug = models.SlugField(
        max_length=250,
        unique_for_date='when_published'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    when_published = models.DateTimeField(
        default=timezone.now
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    category = models.ForeignKey(
        Categories,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='back_to_posts',
        default='none'
    )

    def __str__(self):
        return self.title
