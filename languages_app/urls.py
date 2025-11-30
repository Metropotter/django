from django.urls import path
from . import views
from . import auth_views, forum_views 

app_name = 'languages_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('popular/', views.popular_languages, name='popular_languages'),
    path('language/<int:language_id>/', views.language_detail, name='language_detail'),
   # AUTH URLs 
    path('register/', auth_views.register, name='register'),
    path('login/', auth_views.user_login, name='user_login'),  
    path('logout/', auth_views.user_logout, name='user_logout'), 
    path('verify-email/<str:token>/', auth_views.verify_email, name='verify_email'),
    
    # FORUM URLs
    path('forum/', forum_views.forum_home, name='forum_home'),
    path('forum/ask/', forum_views.ask_question, name='ask_question'),
    path('forum/question/<int:question_id>/', forum_views.question_detail, name='question_detail'),
    path('forum/question/<int:question_id>/comment/', forum_views.add_comment, name='add_comment'),
]