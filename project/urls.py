"""
URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
"""
from django import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('cabinet/', admin.site.urls),
    path('chat/', include('apps.chat.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('media/', views.static.serve),
    path('profile/', include('apps.profile.urls')),
    path('', include('apps.index.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
