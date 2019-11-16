from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('page/<str:page_title>/', views.page, name='page'),
    path('db', views.db, name='db')
]
