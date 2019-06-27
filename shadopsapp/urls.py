from django.conf.urls import url
from shadopsapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'base/$', views.about, name='base')
]