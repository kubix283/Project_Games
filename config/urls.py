from django.contrib import admin
from django.conf.urls.static import static

from django.urls import path, include

from django.conf import settings

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps

    path('', include('pages.urls')),
    path('orders/', include('orders.urls')),
    path('games/', include('games.urls')),
    path('forum/', include('forum.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

