from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='quiz'

urlpatterns = [
    path('', views.main, name='main'),
    path('clubs/', views.clubs, name='clubs'),
    path('national/', views.national, name='national')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
