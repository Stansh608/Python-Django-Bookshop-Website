from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_txt=models.CharField("Question Text", max_length=200)
    pub_date=models.DateTimeField("date published")
    
    def __str__(self):
        return self.question_txt
    
    
    def recently_added(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)
        

class Answers(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_txt=models.CharField(max_length=150)
    votes= models.IntegerField(default=0)
    
    def __str__(self):
        return self.answer_txt
    