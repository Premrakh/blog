from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('blog_post/', blog_post, name='blog_post'),
    path('blog_single/<int:pk>', blog_single, name='blog_single'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add_contact/', add_contact, name='add_contact'),
    path('option/', option, name='option'),
    path('subject/<str:pk>', subject, name='subject'),
    path('search/', search ,name='search')
]
