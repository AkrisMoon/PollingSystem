from django.contrib import admin
from django.urls import path, include
import pollingSystem.urls
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/', include(pollingSystem.urls)),
]

urlpatterns += doc_urls