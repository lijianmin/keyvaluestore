from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^object/$', views.keyvalue.as_view(), name='keyvalue'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','html'])