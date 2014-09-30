from django.contrib import admin
from lifehacks.models import LifeHackImage, Tag, TagLifeHackImage

class TagLifeHackImageInline(admin.TabularInline):
    model = TagLifeHackImage

class LifeHackImageAdmin(admin.ModelAdmin):
    list_display = (
        'url',
        'name',
        'preview_image_url',
        'show',
        )
    readonly_fields = ("url", "preview_image_url", "thumbnail")
    inlines = [TagLifeHackImageInline]
    list_filter = ('show', 'tags')
    search_fields = ['name']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(LifeHackImage, LifeHackImageAdmin)
admin.site.register(Tag, TagAdmin)

