from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('metas/', include('tasks.urls')),
    path('about/', include('about.urls')),
    path('metas/', include('tasks.urls')),
]
