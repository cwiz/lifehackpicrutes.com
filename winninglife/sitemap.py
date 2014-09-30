from django.contrib import sitemaps
from django.core.urlresolvers import reverse
import datetime

class StaticSitemap(sitemaps.Sitemap):
    def __init__(self, names):
        self.names = names

    def items(self):
        return self.names

    def changefreq(self, obj):
        return 'daily'

    def lastmod(self, obj):
        return datetime.datetime.now()

    def location(self, obj):
        return reverse(obj)

class ModelSitemap(StaticSitemap):
    def __init__(self, name, objects):
        self.name = name
        self.objects = objects

    def items(self):
        return [o.pk for o in self.objects]

    def location(self, obj):
        return reverse(self.name, args=[obj])


# actual sitemaps

from lifehacks.models import LifeHackImage

lifehack_image_sitemap  = ModelSitemap('lifehack', LifeHackImage.objects.filter(show=True))
static_sitemap          = StaticSitemap(['home', 'categories', 'new'])
