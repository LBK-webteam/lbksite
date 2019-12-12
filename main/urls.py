from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('page/<str:page_title>/', views.page, name='page'),
    path('db', views.db, name='db'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
