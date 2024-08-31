from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home_page, name="home"),

    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('logout/', views.logout_user, name="logout"),

    path('dashboard/', views.dashboard, name="dashboard"),

    path('job/<str:pk>/', views.job_page, name="job"),
    path('jobs/', views.jobs_page, name="jobs"),
    path('job-post/', views.job_post, name="job-post"),
    path('job-update/<str:pk>/', views.job_update, name="job-update"),
    
]