from django.db import models


class Tag(models.Model):
    name        = models.CharField(max_length=100)
    parent_tag  = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class LifeHackImage(models.Model):
    LANGUAGES = (
        ('RU', 'Russian'),
        ('EN', 'English'),
    )

    url         = models.CharField(max_length=512)
    thumbnail   = models.CharField(max_length=512)

    name        = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    language    = models.CharField(max_length=2, choices=LANGUAGES)
    tags        = models.ManyToManyField(Tag, through='TagLifeHackImage')

    show        = models.BooleanField(default=False)

    def __unicode__(self):
        return self.url

    def preview_image_url(self):
        return '<a href="%s?dl=false"><img src="%s?dl=false" /></a>' % (self.url, self.thumbnail)

    preview_image_url.short_description = 'Thumbnail'
    preview_image_url.allow_tags = True


class TagLifeHackImage(models.Model):
    tag         = models.ForeignKey('Tag')
    image       = models.ForeignKey('LifeHackImage')


class Subscriber(models.Model):
    email       = models.EmailField(max_length=254)