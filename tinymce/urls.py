# Copyright (c) 2008 Joost Cassee
# Licensed under the terms of the MIT License (see LICENSE.txt)

try:
    from django.conf.urls import url, patterns
    v110plus = False
except:
    try:
        from django.conf.urls.defaults import *
        v110plus = False
    except:
        from django.conf.urls import url
        v110plus = True

if v110plus:
    from . import views
    urlpatterns = [
        url(r'^js/textareas/(?P<name>.+)/$', views.textareas_js, name='tinymce-js'),
        url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', views.textareas_js, name='tinymce-js-lang'),
        url(r'^spellchecker/$', views.spell_check),
        url(r'^flatpages_link_list/$', views.flatpages_link_list),
        url(r'^compressor/$', views.compressor, name='tinymce-compressor'),
        url(r'^filebrowser/$', views.filebrowser, name='tinymce-filebrowser'),
        url(r'^preview/(?P<name>.+)/$', views.preview, name='tinymce-preview'),
    ]
else:
    urlpatterns = patterns('tinymce.views',
        url(r'^js/textareas/(?P<name>.+)/$', 'textareas_js', name='tinymce-js'),
        url(r'^js/textareas/(?P<name>.+)/(?P<lang>.*)$', 'textareas_js', name='tinymce-js-lang'),
        url(r'^spellchecker/$', 'spell_check'),
        url(r'^flatpages_link_list/$', 'flatpages_link_list'),
        url(r'^compressor/$', 'compressor', name='tinymce-compressor'),
        url(r'^filebrowser/$', 'filebrowser', name='tinymce-filebrowser'),
        url(r'^preview/(?P<name>.+)/$', 'preview', name='tinymce-preview'),
    )
