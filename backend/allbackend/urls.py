from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('farewell/api/', include('farewell.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
