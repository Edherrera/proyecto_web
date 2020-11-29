"""añadi esto nuevo"""
from django.conf.urls import url

from apps.acudiente.views import index_acudiente

urlpatterns = [
   url(r'^$', index_acudiente)
]