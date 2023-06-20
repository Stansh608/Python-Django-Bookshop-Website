from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import loader
# to use render from django.shortcuts
from django.shortcuts import render

# Return the 404 Error if the Questions are present
from django.shortcuts import get_object_or_404

# Create your views here.

def hello(request):
    return HttpResponse('Welcome to Django. The road has just begun')

def each_quiz(request, quiz_id):
    # if not found, return HTTP 404 Error.
    the_quiz=get_object_or_404(Question, pk=quiz_id)
    #detail_template=loader.get_template('bookshop/detail.html')
    
    content={
        'each_quiz': the_quiz
    }
  
        
    return render(request, 'bookshop/detail.html', content)

def get_questions(request):
    # list the questions from the latest date (5)
    latest_quiz_list=Question.objects.order_by('-pub_date')[:5]
    
    #cast to template
    template= loader.get_template('bookshop/index.html')
    
    context={
        "latest_quiz_list": latest_quiz_list,
    }
    # # loop through to return a string
    # response= '\t'.join([q.question_txt for q in latest_quiz_list])
    
    return HttpResponse(template.render(context, request))
def get_quiz_easily(request):
    all_quiz=Question.objects.order_by('-pub_date').all()
    
    #pass data to the template
    context={
        "latest_quiz_list":all_quiz,
    }
    
    return render(request, 'bookshop/index.html', context)

