from django.shortcuts import render
from django.http import HttpResponse


def index(request):
   # latest_question=Question.objects.order_by('-pub_date')[:5]

    return HttpResponse("Hello world")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

