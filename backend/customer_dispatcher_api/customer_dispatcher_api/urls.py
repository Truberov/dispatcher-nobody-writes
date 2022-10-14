from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('core.urls')),

    re_path(r"^api/auth/", include("djoser.urls.jwt")),
]
