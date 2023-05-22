from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='quiz'

urlpatterns = [
    path('', views.main, name='main'),
    path('clubs/', views.clubs, name='clubs'),
    path('national/', views.national, name='national'),
    path('<str:quiz_type>/result', views.result, name='result'),
    path('profile/<int:user_id>', views.profile, name='profile')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
