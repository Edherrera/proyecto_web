"""añadi esto nuevo"""
from django.conf.urls import url, include 

from apps.alumna.views import index




urlpatterns = [
    url(r'^$', index),
]