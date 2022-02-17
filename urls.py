from django.urls import include, path

urlpatterns = [
    path('', include('wk.urls', namespace="well-known")),
]
