from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('make_appointment/', views.make_appointment, name='make_appointment'),
    path('about', views.about, name='about'),
    path('services', views.service_view, name='service_view'),
    path('portfolio', views.Portfolio_view, name='Portfolio_view'),
    path('Package_view', views.Package_view, name='Package_view'),
    path('blogs', views.blog_view, name='Blog_view'),
    path('contact', views.contact_view, name='contact_view'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('enquiry', views.enquiry, name='enquiry'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

