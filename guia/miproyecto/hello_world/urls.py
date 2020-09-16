from django.contrib import admin
from django.urls import path
from pages import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.home_page_view),
    path('home', views.home_page_view),
]