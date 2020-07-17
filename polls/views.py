from django.http import HttpResponse,HttpResponseRedirect,Http404,request
from django.shortcuts import render
from django.urls import reverse
from .models import Question,Choice
from django.template import loader
# Create your views here.

def index(request):
    q_list = Question.objects.order_by('pub_date')[:5]
    # output = [q.question_text for q in q_list]
    # html = ','.join(output)
    # return HttpResponse("Hello,world. You're at the polls site")
    # return HttpResponse(html)

    return render(request, 'polls/index.html',{'q_list': q_list} )

def index2(request):

    return render(request, 'polls/index2.html',{} )



def login(request):
    return render(request, 'polls/login.html')

def login_post(request):
    user_id = request.GET.get('user_id')
    user_pw = request.GET.get('user_pw')
    print(user_id, user_pw)
    request.session['user_id'] = user_id
    return HttpResponse("로그인 완료")

def logout(request):
    # request.session['user_id'] =None
    request.session.clear()
    return HttpResponse('logout')


def detail(request, question_id): # 질문 상세 페이지
    #                             pk
    question = Question.objects.get(id=question_id);
    return render(request, 'polls/detail.html',{'question': question} )

def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): # 투표 페이지
    choice_id = request.POST['choice']

    #request.POST.get['choice']
    #질문조회
    question = Question.objects.get(id=question_id)
    #보기조회
    choice = question.choice_set.get(id=choice_id)
    #투표수 증가 
    choice.votes += 1
    
    #저장
    choice.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
    #return HttpResponseRedirect('/polls/%s/' % question_id)

def reset(request, question_id):
   
    #질문조회
    question = Question.objects.get(id=question_id)
    #보기조회
    choice_list = question.choice_set.all()

    for choice in choice_list:
        choice.votes = 0
 
    #저장
    choice.save()
    return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
    #return HttpResponseRedirect('/polls/%s/' % question_id)