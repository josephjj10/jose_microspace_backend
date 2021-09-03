from django.urls import path
from . views import Create_register
app_name = 'class'
urlpatterns = [
    path('Create_register',Create_register, name='Create_register'),
]