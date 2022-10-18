from django.db import models
from crawling import do_crawl
# Create your models here.
class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Aquainfo(models.Model):
    date = models.DateTimeField()
    days = models.IntegerField()
    num = models.IntegerField()
    average_weight = models.FloatField()
    total_weight = models.FloatField()
    biomass = models.FloatField()
    survival_rate = models.FloatField()
    feed = models.FloatField()
    weekly_growth_rate = models.FloatField()
    total_weight_increase = models.FloatField()
    feed_conversion_rate = models.FloatField()
    remarks = models.TextField()

"""
class Sealife(models.Model):
    title = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    content = models.TextField()
    def __init__(self):
        data = do_crawl()
        self.title = data['title']
"""