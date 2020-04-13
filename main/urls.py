from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
HEAD: object
urlpatterns = [
    path('', views.home, name='home'),
    path('page/<str:page_title>/', views.page, name='page'),
    path('db', views.db, name='db'),
    # path('galabal', views.galabal, name='galabal'),
    path('success', views.success, name='success'),
    path('br/algemeen', views.br_algemeen, name='br_algemeen'),
    path('br/bedrijven', views.br_bedrijven, name='br_bedrijven'),
    path('br/galerij', views.br_galerij, name='br_galerij'),
    path('br/vacatures', views.br_vacatures, name='br_vacatures'),
    path('opkomend/formulieren', views.opkomend_formulieren, name='opkomend_formulieren'),
    path('opkomend/brieven', views.opkomend_brieven, name='opkomend_brieven'),
    path('neucom', views.neucom, name='neucom'),
    path('officiele_documenten', views.officiele_documenten, name='officiele_documenten'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
