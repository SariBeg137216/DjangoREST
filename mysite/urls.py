from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieView, ComedyView

router = routers.SimpleRouter()
router.register('movies', MovieView)
router.register('comedy', ComedyView)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('index/', include('movies.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

