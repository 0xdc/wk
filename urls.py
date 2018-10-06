from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('wk.urls', namespace="well-known")),
]
