from django.urls import path
from . import views

urlpatterns = [
    path("", views.startPage, name="start"),
    path("home/", views.home, name="home"),
    path("login/", views.loginToAcc, name="login"),
    path("logout/", views.logoutFromAcc, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("changePassword/", views.changePassword, name='changePassword'),
    path("statistics/", views.statistics, name="statistics"),
    path("statistics/<str:player_nick>/", views.player_stats, name="player_stats"),
    path("statistics/maps/<str:the_map>/", views.map_stats, name="map_stats"),
]
