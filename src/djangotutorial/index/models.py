import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category


class Content(models.Model):
    content_title = models.CharField(max_length=200)
    content_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField("date published")
    category = models.ForeignKey(
        Category,
        models.PROTECT, 
        related_name='contents'
    )

    def __str__(self):
        return self.content_title

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
