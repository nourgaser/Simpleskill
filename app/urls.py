from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    
    
    # choose interests for the first time or update them
    path('choose_categories', views.choose_categories, name='choose_categories'),
    
    # set your experience level for the first time or update it for your fields of interest (categories)
    path('experience_level', views.experience_level, name='experience_level'),
    
    # set your experience level for the first time or update it for your fields of interest (categories)
    path('interest_level', views.interest_level, name='interest_level'),
    
    # overview of all your registered simpleskills, your progress
    path('dashboard', views.dashboard, name='dashboard'),
    
    #learn a registered simpleskill (view material and track progress here)
    path('learn/<int:ssid>', views.learn, name='learn'),
    
    # explore new simpleskills (recommendations, search and filters)
    path('explore', views.explore, name='explore'),
]
