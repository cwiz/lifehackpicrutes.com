from django.conf.urls import patterns, include, url
from django.contrib import admin
from sitemap import lifehack_image_sitemap, static_sitemap

admin.autodiscover()


sitemaps = {
    'pages': static_sitemap,
    'images': lifehack_image_sitemap
}


urlpatterns = patterns('',
    url(r'^$', 						'lifehacks.views.index', 		name='home'),
    url(r'^admin/', 				include(admin.site.urls)),
    url(r'^api/v0/add_file/$', 		'lifehacks.views.api_add_file', name='api_add_file'),
    url(r'^categories/', 			'lifehacks.views.categories', 	name='categories'),
    url(r'^new/', 					'lifehacks.views.new', 			name='new'),
    url(r'^category/(?P<id>\d+)/$', 'lifehacks.views.category', 	name='category'),
    url(r'^lifehack/(?P<id>\d+)/$', 'lifehacks.views.lifehack', 	name='lifehack'),
    url(r'^random/', 				'lifehacks.views.random', 		name='random'),  
    url(r'^search?/',                'lifehacks.views.search',       name='search'),  
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
)