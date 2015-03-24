from django.conf.urls import patterns, include, url
from django.contrib import admin
import partymaker.views as pmviews

urlpatterns = patterns('',
    url(r'^/?$',pmviews.welcome),
    url(r'animal/?$',pmviews.list_animals),
    url(r'animal/json/?$',pmviews.list_animals_json),
    url(r'animal/new/?$',pmviews.create_animal),
    url(r'animal/(\d+)/?$',pmviews.view_animal),
    url(r'animal/(\d+)/edit/?$',pmviews.edit_animal),
    url(r'neighborhood/?$',pmviews.list_neighborhoods),
    url(r'neighborhood/new/?$',pmviews.create_neighborhood),
    url(r'neighborhood/(\d+)/?$',pmviews.view_neighborhood),
    url(r'neighborhood/(\d+)/edit/?$',pmviews.edit_neighborhood),
    url(r'^admin/', include(admin.site.urls)),
)
