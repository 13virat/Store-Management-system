"""
URL configuration for djangoproject project.

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
from django.urls import path
from stockmgmt import views

urlpatterns = [
    path('', views.home, name='home'),
    path("list_items/", views.list_items, name='list_items'),
    path("add_items/", views.add_items, name='add_items'),
    # path("delete_items/", views.delete_items, name='delete_items'),
    # path("update_items/", views.update_items, name='update_items'),
    # path("search_items/", views.search_items, name='search_items'),
    # path("stock_items/", views.stock_items, name='stock_items'),
    path("admin/", admin.site.urls),
]
