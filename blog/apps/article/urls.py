from django.urls import path
from blog.apps.article import views

app_name = 'article'
urlpatterns = [
    path('', views.home, name='home'),
    path('add-article/', views.CreateNewArticle.as_view(), name='add-article'),
    path('edit-article/', views.EditArticle.as_view(), name='edit-article'),
]
