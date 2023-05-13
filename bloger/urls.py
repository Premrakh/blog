from django.urls import path
from .views import *
urlpatterns = [
    path('', bloger_index, name='bloger_index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('add_blog/', add_blog, name='add_blog'),
    path('otp/', otp, name='otp'),
    path('logout/', logout, name='logout'),
    path('connect/', connect, name='connect'),
    path('edit_blog/<int:pk>', edit_blog, name='edit_blog'),
    path('del_blog/<int:pk>', del_blog, name='del_blog'),

]