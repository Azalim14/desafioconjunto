from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('metas.urls')),
    path('about/', include('about.urls')),
    path('users/', include('users.urls')),
]
