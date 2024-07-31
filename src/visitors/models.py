from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.
class PageVisitors(TimeStampedModel):
    path = models.TextField(max_length=250, null=True, blank=True)