from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('quizes.urls', namespace='quizes')),
    path('api/v1/', include('api.urls', namespace='api')),
    path('users/', include('users.urls', namespace='users')),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
