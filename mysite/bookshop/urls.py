from django.urls import path
from . import views

app_name="bookshop"
urlpatterns = [
    
    path('', views.questions, name="question"), # Launch to all question
    
    path('<int:quiz_id>/', views.each_quiz, name="each_quiz"), # each question with answers and option to vote
    
    path('<int:quiz_id>/vote', views.vote, name="vote"), # Vote action
    
    path('<int:quiz_id>/results', views.results, name="results"),  # Results after voting
    
    
    
]
