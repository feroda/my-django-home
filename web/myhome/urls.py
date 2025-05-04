from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings

from rest_framework import routers

from web.views.api import ArtistQuoteViewSet, ProjectViewSet


router = routers.SimpleRouter()
router.register(r'api/v1/artistquotes', ArtistQuoteViewSet)
router.register(r'api/v1/projects', ProjectViewSet)


def page_view(template_name):
    # TODO: decorator for custom headers?
    return TemplateView.as_view(template_name=template_name, http_method_names=["get"])
# WAS: return login_required(TemplateView.as_view(template_name=template_name, http_method_names=["get"]))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', page_view("web/index.html"), name="index"),
    path('iframes/4d-me/', TemplateView.as_view(template_name="web/4dme.html"), name="4d-me"),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
