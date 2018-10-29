from django.conf.urls import url

from . import views

app_name = "well-known"
urlpatterns = [
    url(r'^openpgpkey/hu/(?P<tgt>.*)$', views.wkd, name="wkd"),
    url(r'^(?P<tgt>.*)$', views.view, name="view"),
]
