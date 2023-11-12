"""
URL configuration for geodjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from assignment1.views import redirect_to_pine_martens

#from assignment1.views import redirect_to_login





urlpatterns = [
 #'   path('', redirect_to_login, name='redirect-to-login'),
    path('', redirect_to_pine_martens, name='redirect-to-pine-martens'),
    path('admin/', admin.site.urls),
  #  path("assignment1/", include("django.contrib.auth.urls")), 
    path('assignment1/', include('assignment1.urls')),

]