from django.shortcuts import render
from django.http import HttpResponse
#from django.template import RequestContext, loader
#from django.http import Http404
#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
#from . models import Answer, Question
#import random
#import datetime
#from django.utils.encoding import *



# Create your views here.


# Note the index page used in the index function below tells the computer
# user about the application and what it is meant to be used for

def index(request):
    return render(request, 'index.html')
