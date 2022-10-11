from django.db import models
from crawling import do_crawl
# Create your models here.
class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

"""
class Sealife(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    def __init__(self):
        data = do_crawl()
        self.title = data['title']
"""