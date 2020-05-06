from django.db import models
from datetime import datetime
from django.conf import settings
# Create your models here.

class Join(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='join_users',
        on_delete=models.CASCADE
    )
    time = models.TimeField()

class Dismiss(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='dismiss_users',
        on_delete=models.CASCADE
    )

class JoinMatch(models.Model):
    home_away = models.CharField(max_length=10)
    league_acl_fa = models.CharField(max_length=10)
    vs = models.CharField(max_length=20)
    date = models.DateTimeField()

    content = models.TextField(default='')

    join_match = models.ManyToManyField(
        Join,
        related_name='join_matches'
    )
    dismiss_match = models.ManyToManyField(
        Dismiss,
        related_name='dismiss_matches'
    )

    def d_day(self):
        return (self.date.replace(tzinfo=None)-datetime.utcnow()).days + 2
