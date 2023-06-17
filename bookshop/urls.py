from django.urls import path
from . import views

app_name="bookshop"
urlpatterns = [
    path('', views.hello, name='hello'),  
    path('questions/', views.get_questions, name="question"),
    path('each_quiz/<int:quiz_id>/', views.each_quiz, name="each_quiz"),
    path('quick_quizes',views.get_quiz_easily, name='quick-questions'),
    
]
