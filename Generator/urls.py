from django.urls import path
from .views import *

app_name = 'Generator'

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about_me, name='about'),
    path('generate/', generate, name='generate'),
    path('backward/', backward, name='backward'),
    path('backward/result/', backward_result, name='backward_result'),
]
