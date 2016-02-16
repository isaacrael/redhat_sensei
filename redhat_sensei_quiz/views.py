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



# Create your views here.


# Note the index page used in the index function below tells the computer
# user about the application and what it is meant to be used for

def index(request):
    return render(request, 'index.html')

def quiz_selection(request):
    return render(request, 'redhat_sensei_quiz/quiz_selection.html')

def git_quiz(request):
    if request.method == 'POST':
        gils_answer = request.POST.get('textfield', None)
    elif request.method != 'POST':
        gils_answer == "None"
    if gils_answer == '1':
        temp_latest_question_list = Question.objects.filter(category="Account Administration")
    if gils_answer == '2':
        temp_latest_question_list = Question.objects.filter(category="UNIX Commands")
    if gils_answer == '3':
        temp_latest_question_list = Question.objects.filter(category="Networking")
    latest_question_list = temp_latest_question_list


    #value = smart_text(user_answer)
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
def git_quiz(request):
#    if request.method == 'POST':
    user_answer = request.POST.get('textfield', None)
        # Get the question object
#        q = Question.objects.get(pk=question_id)
        # Get all the answers associated with the question object
#        a = q.answer_set.all()
        # Get the first element in the list of answers
#        value = a[0]
        # smart_text is a django utility that converts an object to a unicode string
#        correct_answer = smart_text(value)
#        context = {'latest_question_list': latest_question_list, 'answer': user_answer, 'question': question, 'correct_answer': correct_answer}
#        value = "gil"

#    value = latest_question_list[0]
#    q = smart_text(value)
    context = {'answer': user_answer}
    return render(request, 'redhat_sensei_quiz/index.html', context)
"""






#def git_resources(request):
#        return render(request, 'giturdone_quiz/resources.html')


"""
def detail(request, textfield):
    if request.method == 'POST':
        user_answer = request.POST.get('textfield', None)
    if user_answer == 'Account Administration':
       latest_question_list = 'True'
    else:
       latest_question_list = 'False'
    context = {'latest_question_list': latest_question_list, 'answer': user_answer}
    return render(request, 'redhat_sensei_quiz/detail.html', context)
"""



"""
# Note: The answer function below is not being used but is left here
# as an example for future versions of the application and may be able
# to be used to implement a way to show a computer users test score based
# on the number of questions answered correctly vs. total questions responded to

def answer(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question answer form.
        return render(request, 'giturdone_quiz/detail.html', {
            'question': p,
            'error_message': "You didn't select an answer.",
        })
    else:
        selected_choice.answers += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('giturdone_quiz:results', args=(p.id,)))

"""










"""
def results(request):
    if request.method == 'POST':
        user_answer = request.POST.get('textfield', None)
    if user_answer == 'Account Administration':
       latest_question_list = 'True'
    else:
       latest_question_list = 'False'
    context = {'latest_question_list': latest_question_list, 'answer': user_answer}
    return render(request, 'redhat_sensei_quiz/results.html', context)
"""