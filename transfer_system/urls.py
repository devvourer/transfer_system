from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('custom_auth.urls')),
    path('wallet/', include('wallet.urls')),
]
