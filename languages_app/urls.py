from django.urls import path
from . import views

app_name = 'languages_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('popular/', views.popular_languages, name='popular_languages'),
    path('language/<int:language_id>/', views.language_detail, name='language_detail'),
]