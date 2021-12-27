from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

from django.conf import settings

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')), # new

    # Local apps
    path('', include('pages.urls')),
    path('games/', include('games.urls')), # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
