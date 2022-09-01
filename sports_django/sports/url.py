from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('teams/', views.player_list, name='player_list'),
    path('team/<int:pk>', views.team_detail, name='team_detail'),
    path('player/<int:pk>', views.player_detail, name='player_detail')
]