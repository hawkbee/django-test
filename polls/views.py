from django.shortcuts import render, Http404, get_object_or_404

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render({'latest_question_list': latest_question_list}, request))
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question': question, 'error_message': "You din't select a choice."})
    else:
        choice.votes += 1
        choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
