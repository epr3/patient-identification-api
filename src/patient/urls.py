"""patient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from custom_authentication import views as auth_views
from patient_summary import views as summary_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.Login.as_view()),
    path('logout/', auth_views.Logout.as_view()),
    path('test/', summary_views.HelloView.as_view())
]
