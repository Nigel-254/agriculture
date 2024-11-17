from django.contrib import admin
from django.urls import path

from application import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('index/', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
]