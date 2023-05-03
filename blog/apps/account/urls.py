from django.urls import path
from blog.apps.account import views

app_name = 'account'
urlpatterns = [
    path('login/', views.author_login, name='login'),
    path('logout/', views.author_logout, name='logout'),
    path('profile/', views.profile, name='profile')
]
