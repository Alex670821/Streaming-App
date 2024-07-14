# auth_system/urls.py
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/subscription/", include("subscriptions.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    path("directos/", include("directos.urls")),
    path('accounts/', include('accounts.urls')),
    path('rewards/', include('rewards.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r"^.*", TemplateView.as_view(template_name="index.html"))]
