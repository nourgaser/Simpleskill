from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    path('configure/', views.configure, name='configure_index'),
    

    # choose interests for the first time or update them
    path('configure/interests', views.configure_interests, name='configure_interests'),
    
    # set your experience level for the first time or update it for your fields of interest (categories)
    path('configure/experience_level', views.experience_level, name='configure_experience_level'),
    
    # set your experience level for the first time or update it for your fields of interest (categories)
    path('configure/interest_level', views.interest_level, name='configure_interest_levels'),
    
    # overview of all your registered simpleskills, your progress
    path('<int:fid>', views.dashboard, name='dashboard'),
    
    #learn a registered simpleskill (view material and track progress here)
    path('learn/<int:ssid>', views.learn, name='learn'),
    
    # explore new simpleskills (recommendations, search and filters)
    path('explore', views.explore, name='explore'),
]
