"""TextStatistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from appTextStats.views import perform_stats,perform_removeChar,perform_specialChar

app_name = 'appTextStats'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('textstats/',perform_stats),
    path('removechar/',perform_removeChar),
    path('specialchar/',perform_specialChar),
]
