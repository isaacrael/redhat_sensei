from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from . models import Answer, Question
import random
import datetime
from django.utils.encoding import *
# The line below imports the user_response variable from the user_response.py file
from . user_response import gils_answer



# Create your views here.


# Note the index page used in the index function below tells the computer
# user about the application and what it is meant to be used for

def index(request):
    return render(request, 'index.html')

def quiz_selection(request):
    if request.method == 'POST':
        user_response = request.POST.get('textfield', None)
        user_response = smart_text(user_response)
        f = open('redhat_sensei_quiz/user_response.py', 'w')
        # the line below write the text 'gils_answer = ' and appends the user_response the str function gets rid of u in front of string
        f.write('gils_answer = ' + repr(str(user_response)))
        f.close()
    return render(request, 'redhat_sensei_quiz/quiz_selection.html')

def git_quiz(request):
    if gils_answer == 'None':
        return render(request, 'redhat_sensei_quiz/index.html')
    if gils_answer == '1':
        latest_question_list = Question.objects.filter(category="User Management")
    if gils_answer == '2':
        latest_question_list = Question.objects.filter(category="UNIX Commands")
    if gils_answer == '3':
        latest_question_list = Question.objects.filter(category="Networking")
    context = {'gils_answer': gils_answer, 'latest_question_list': latest_question_list}
    return render(request, 'redhat_sensei_quiz/index.html', context)


def account_administration(request):
    account_administration_question_list = Question.objects.filter(category="Account Administration")
#    value = latest_question_list[0]
#    q = smart_text(value)
    context = {'account_administration_question_list': account_administration_question_list}
    return render(request, 'redhat_sensei_quiz/account_administration.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'redhat_sensei_quiz/detail.html', {'question': question})

def results(request, question_id):
    latest_question_list = Question.objects.order_by('?')
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        user_answer = request.POST.get('textfield', None)
        # Get the question object
        q = Question.objects.get(pk=question_id)
        # Get all the answers associated with the question object
        a = q.answer_set.all()
        # Get the first element in the list of answers
        value = a[0]
        # smart_text is a django utility that converts an object to a unicode string
        correct_answer = smart_text(value)
        context = {'latest_question_list': latest_question_list, 'answer': user_answer, 'question': question, 'correct_answer': correct_answer}
        value = "gil"
    return render(request, 'redhat_sensei_quiz/results.html', context)


"""

def results(request, question_id):
    account_administration_question_list = Question.objects.order_by('?')
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        user_answer = request.POST.get('textfield', None)
        # Get the question object
        q = Question.objects.get(pk=question_id)
        # Get all the answers associated with the question object
        a = q.answer_set.all()
        # Get the first element in the list of answers
        value = a[0]
        # smart_text is a django utility that converts an object to a unicode string
        correct_answer = smart_text(value)
        context = {'account_administration_question_list': account_administration_question_list, 'answer': user_answer, 'question': question, 'correct_answer': correct_answer}
        value = "gil"
    return render(request, 'redhat_sensei_quiz/results.html', context)


"""


#def git_resources(request):
#        return render(request, 'giturdone_quiz/resources.html')





