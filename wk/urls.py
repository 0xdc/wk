from django.urls import path, re_path

from . import views

app_name = "well-known"
urlpatterns = [
    path('openpgpkey/hu/<tgt>', views.wkd, name="wkd"),
    re_path(r'^(?P<tgt>.*)$', views.view, name="view"),
]
