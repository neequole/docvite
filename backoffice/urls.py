from django.conf.urls import url, include

from .api import urls


urlpatterns = [
    url(r"", include(urls)),
]