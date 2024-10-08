"""
URL configuration for Kate_Tracking project.

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
from Tracking import views as tracking_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',tracking_views.index_view,name='index'),
    path('login', tracking_views.login_view, name='login'),
    path('logout', tracking_views.logout_view, name='logout'),
    path('new_participant', tracking_views.new_participant_view, name='new_participant'),
    path('participants/', tracking_views.participants_view, name='participants'),
    path('entry', tracking_views.participant_entry_view, name='entry'),
    path('api/',include('api.urls')),
    path('participant/<int:id>',tracking_views.participant_info_view, name='info')
]
