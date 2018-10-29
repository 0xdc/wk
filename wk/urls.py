from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^openpgpkey/hu/(?P<tgt>.*)$', views.wkd, name="wkd"),
    url(r'^(?P<tgt>.*)$', views.view, name="view"),
]
