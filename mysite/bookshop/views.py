from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Answers
from django.template import loader


# to use render from django.shortcuts
from django.shortcuts import render

# Return the 404 Error if the Questions are present
from django.shortcuts import get_object_or_404

from django.urls import reverse



# Create your views here.

def hello(request):
    return HttpResponse('Welcome to Django. The road has just begun')


# using loader to fetch the template via get_template() method

def questions(request):
    # list the questions from the latest date (5)
    latest_quiz_list=Question.objects.order_by('-pub_date')[:5]
    
    # #cast to template
    # template= loader.get_template('bookshop/index.html')
    
    # context={
    #     "latest_quiz_list": latest_quiz_list,
    # }
    # # # loop through to return a string
    # # response= '\t'.join([q.question_txt for q in latest_quiz_list])
    
    # return HttpResponse(template.render(context, request))
    return render(request, "bookshop/index.html", {
        "latest_quiz_list": latest_quiz_list,
    })


# display each question and the associated answer
def each_quiz(request, quiz_id):
    # if not found, return HTTP 404 Error.
    the_quiz=get_object_or_404(Question, pk=quiz_id)
    #detail_template=loader.get_template('bookshop/detail.html')
    
    content={
        'each_quiz': the_quiz
    }
  
        
    return render(request, 'bookshop/each_quiz.html', content)


def vote(request, quiz_id):
    print(quiz_id)
    question = get_object_or_404(Question, pk=quiz_id)
    try:
        selected_answer = question.answers_set.get(pk=request.POST["ans"])
    except (KeyError, Answers.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "bookshop/each_quiz.html",
            {
                "each_quiz": question,
                "error_message": "You didn't select an answer.",
            },
        )
    else:
        selected_answer.votes += 1
        selected_answer.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        # using the HttpResponseRedirect() which takes 1 positional arguement "url" to the redirecting page optionall args can be given too as below.
        return HttpResponseRedirect(reverse("bookshop:results", args=(question.id,)))
    
    
    
def results(request, quiz_id):
    question = get_object_or_404(Question, pk=quiz_id)
    return render(request, "bookshop/results.html", {"question": question})
