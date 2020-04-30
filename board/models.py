from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from datetime import datetime
# Create your models here.
class Board(models.Model) :
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=30)
    choice = models.CharField(max_length=10)
    content = RichTextUploadingField(
        blank=True, null=True,
        config_name='special',
        external_plugin_resources=[(
            'youtube',
            '/static/board/ckeditor_plugins/youtube/youtube/',
            'plugin.js'
            ),
            (
            'html5video',
            '/static/board/ckeditor_plugins/html5video/html5video/',
            'plugin.js'
            )
            ]
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_boards'
    )
    dislike_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='dislike_boards'
    )
    hit = models.IntegerField(default=0)
    hashtag = models.CharField(max_length=100, null=True)

    def is_updated(self):
        return datetime.utcnow().hour - self.updated_at.hour <= 2

class Hashtag(models.Model):
    board = models.ManyToManyField(
        Board,
        related_name='hashtag_boards'
    )
    content = models.CharField(max_length=100)

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
