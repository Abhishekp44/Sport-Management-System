from django.urls import path
from . import views



urlpatterns = [
    path('',views.coach_login),
    path('register_player/', views.register_player, name='register_player'),
    path('login/', views.coach_login, name='coach_login'),
    path('dashboard/', views.coach_dashboard, name='coach_dashboard'),
    path('logout/', views.coach_logout),
    path('add_schedule/', views.add_schedule, name='add_schedule'),
    path('edit_schedule/<int:id>/', views.edit_schedule, name='edit_schedule'),
    path('delete_schedule/<int:id>/', views.delete_schedule, name='delete_schedule'), 
    path('add_team/', views.add_team, name='add_team'),  
    path('team/<int:id>/', views.team_details, name='team_details'), 
    path('edit_team/<int:id>/', views.edit_team, name='edit_team'), 
    path('delete_team/<int:id>/', views.delete_team, name='delete_team'),  

]
