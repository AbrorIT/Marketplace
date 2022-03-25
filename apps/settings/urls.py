from django.urls import URLPattern, path
from apps.settings.views import index


urlpatterns = [
    path('', index, name="index"),
]