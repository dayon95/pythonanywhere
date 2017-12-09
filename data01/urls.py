from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^test_pd1_time',views.test_pd1_time),
    url(r'^test_pd1_time',views.test_pd2),

    url(r'^test',views.test),
    url(r'^$',views.index, name='index'),
    url(r'^tutorial',views.index_tutorial),
    url(r'^about',views.about, name='about'),
    url(r'^ajax/poster_detail',views.poster_detail,name='poster_detail'),

    url(r'^feedback/$', views.feedback_index),
    url(r'^feedback/(?P<pk>\d+)/$', views.feedback_detail,name='detail'),
    url(r'^feedback/(?P<pk>\d+)/new/$', views.feedback_new,name='new'),

    url(r'^calendar',views.calendar,name='calendar'),
    #카테고리 분류
    url(r'^(?P<category>[\w|\W]+)/$',views.index),
    #url(r'^search/(?P<search>[\w|\W]+)/$',views.poster_search, name='search'),
]
