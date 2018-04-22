from django.contrib import admin
from django.urls import path, includes

urlpatterns = [
    path('', include('waimai.urls')),
    path('admin/', admin.site.urls),
]
