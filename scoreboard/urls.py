from django.urls import path
from . import views


urlpatterns = [
    path('', views.scoreboard, name="scoreboard"),
    path('api2db/', views.api2db, name="api2db"),
    path('time_test/', views.time_test, name="time_test"),
    path('tag_change/<int:id>/', views.tag_change, name="tag_change"),
    path('tag_update/<int:id>/', views.tag_update, name="tag_update"),
]
