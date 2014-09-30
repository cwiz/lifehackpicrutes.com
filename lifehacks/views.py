# Create your views here.
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from lifehacks.models import LifeHackImage, Tag, TagLifeHackImage

import utils

def index(request):
    lifehacks = LifeHackImage.objects.filter(show=True).order_by('?')[:6]

    return render(request, 'lifehacks/index.jade', {
        'lifehacks': lifehacks,
    })


def random(request):
    lifehack_image = LifeHackImage.objects.filter(show=True).order_by('?')[:1][0]
    return redirect(reverse('lifehack', args=[lifehack_image.id]))


def lifehack(request, id):
    image = get_object_or_404(LifeHackImage, id=id)
    return render(request, 'lifehacks/image.jade', {'image': image})


def get_all_images_for_tag(tag, images):
    for tag_image in TagLifeHackImage.objects.filter(tag=tag).select_related('image'):
        images.append(tag_image.image)
    return images


def category(request, id):
    tag = get_object_or_404(Tag, id=id)

    images = get_all_images_for_tag(tag, [])
    for child in tag.tag_set.all():
        images += get_all_images_for_tag(child, images)

    return render(request, 'lifehacks/category.jade', {'images': set(images), 'category': tag,})

def new(request):
    images = LifeHackImage.objects.filter(show=True).order_by('-id')[:20]
    return render(request, 'lifehacks/new.jade', {'images':images})


def categories(request):
    tags = Tag.objects.filter(parent_tag=None).select_related('tag_set').order_by('name')
    rows = utils.make_rows(tags)
    return render(request, 'lifehacks/categories.jade', {'rows': rows})


def api_add_file(request):
    url = request.GET.get('url')
    thumbnail = request.GET.get('thumbnail')

    if not url:
        return HttpResponse('not uploaded')

    lifehack_image = LifeHackImage()
    lifehack_image.url = url
    lifehack_image.thumbnail = thumbnail
    lifehack_image.save()

    return HttpResponse('file saved')


def search(request):
    return render(request, 'search.jade')