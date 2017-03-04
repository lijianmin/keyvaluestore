from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^object/$', views.post_keyvalue.as_view(), name='post_keyvalue'),
    url(r'^object/(?P<key>\w+)$', views.get_keyvalue.as_view(), name='get_keyvalue'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json','html'])