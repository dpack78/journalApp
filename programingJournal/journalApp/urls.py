from django.conf.urls import url

from . import views

app_name = 'journalApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.index, name='index'),
    url(r'^/saveNewDay',views.saveNewDay, name='saveNewDay')
]
