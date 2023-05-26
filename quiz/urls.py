from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='quiz'

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:quiz_type>/result', views.result, name='result'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('ranking/<str:quiz_type>', views.ranking, name='ranking'),
    path('quiz/<str:quiz_type>', views.quiz, name='quiz'),
    path('squad_challange', views.squad_challange, name='squad_challange'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
