from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<tgt>.*)$', views.view, name="view"),
]