"""
URL configuration for basroba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('adminadminadmin/', admin.site.urls),

    # include Django's i18n helpers (gives name='set_language' at /i18n/setlang/)
    path('i18n/', include('django.conf.urls.i18n')),

    # language selection page (we'll create template select_language.html)
    path('choose-language/', TemplateView.as_view(template_name='select_language.html'), name='choose-language'),

    path('', include("app.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
