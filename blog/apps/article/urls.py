from django.urls import path, include
from blog.apps.article import views

app_name = 'article'
urlpatterns = [
    path('a/', views.test.as_view(), name='test'),
]
