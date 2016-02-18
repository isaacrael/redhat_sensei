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
from . user_response import user_response



# Create your views here.


# Note the index page used in the index function below tells the computer
# user about the application and what it is meant to be used for

def index(request):
    return render(request, 'index.html')

# quiz_selection page takes a user_response as input and displays associated quiz on Sensei Quiz page

def quiz_selection(request):
    if request.method == 'POST':
        user_response = request.POST.get('textfield', None)
        user_response = smart_text(user_response)
        f = open('redhat_sensei_quiz/user_response.py', 'w')
        # the line below write the text 'user_response = ' and concats the user_response the str function gets rid of u in front of string
        f.write('user_response = ' + repr(str(user_response)))
        f.close()
    return render(request, 'redhat_sensei_quiz/quiz_selection.html')


# git_quiz displays the quiz selected by user in the Sensei Quiz Selection page

def git_quiz(request):
    if user_response == 'None':
        return render(request, 'redhat_sensei_quiz/index.html')
    if user_response == '1':
        latest_question_list = Question.objects.filter(category="User Management")
    if user_response == '2':
        latest_question_list = Question.objects.filter(category="System Basics")
    if user_response == '3':
        latest_question_list = Question.objects.filter(category="Security & Identity")
    if user_response == '4':
        latest_question_list = Question.objects.filter(category="Basic Configuration")
    if user_response == '5':
        latest_question_list = Question.objects.filter(category="Jobs & Services")
    if user_response == '6':
        latest_question_list = Question.objects.filter(category="Kernel, Boot, & Hardware")
    if user_response == '7':
        latest_question_list = Question.objects.filter(category="Software Management")
    if user_response == '8':
        latest_question_list = Question.objects.filter(category="Filesystem, Volumes, & Disks")
    if user_response == '9':
        latest_question_list = Question.objects.filter(category="Networking")
    if user_response == '10':
        latest_question_list = Question.objects.filter(category="Resource Management")
    if user_response == '11':
        latest_question_list = Question.objects.filter(category="UNIX Commands")
    context = {'user_response': user_response, 'latest_question_list': latest_question_list}
    return render(request, 'redhat_sensei_quiz/index.html', context)


# detail view displays the quiz questions

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'redhat_sensei_quiz/detail.html', {'question': question})

# results pages displays whether answer given by user was correct and also displays the correct answer

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
    return render(request, 'redhat_sensei_quiz/results.html', context)


# resources pages contains videos and websites related to the subject matter

def resources(request):
    return render(request, 'redhat_sensei_quiz/resources.html')





