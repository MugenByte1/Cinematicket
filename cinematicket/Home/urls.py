from django.urls import path
from .views import movie_lst

urlpatterns = [
    path('', movie_lst, name='movie_list'),

]
