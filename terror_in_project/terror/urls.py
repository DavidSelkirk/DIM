from django.conf.urls import patterns, url

from terror import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
	url(r'^game$', views.game, name='game')
)
