from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='calc'),
    url(r'^calculation/$', views.get_mortgage_schedule, name='calc2'),
]


