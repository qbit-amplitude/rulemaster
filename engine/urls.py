from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^v1/health$', views.health, name='health'),
]