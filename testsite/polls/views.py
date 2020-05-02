from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def result(request, question_id):
    response = "You are looking at results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    response= HttpResponse("You are voting for question %s" % question_id)
    return response

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    '''
    Long Form :
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question Does not Exist")
    return render(request,'polls/detail.html', {'question': question}) 

    Shortform
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    Def detail short form'''

# Create your views here.
