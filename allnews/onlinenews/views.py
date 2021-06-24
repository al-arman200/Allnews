from django.shortcuts import render
from django.http      import HttpResponse
from .models import Agency , News
from .bsoup import webScraping as ws

def tag_a(strin):
    strout = '<a href="%s" target="_blank" >%s</a>'%(strin[1], strin[0])
    return strout
        
def index(request):
    latest_news_list_f = News.objects.filter(typenews='f').order_by('-pub_date')[:10]
    latest_news_list_v = News.objects.filter(typenews='v').order_by('-pub_date')[:10]
    latest_news_list_e = News.objects.filter(typenews='e').order_by('-pub_date')[:10]
    latest_news_list_s = News.objects.filter(typenews='s').order_by('-pub_date')[:10]
    outputf           = ', '.join([q.title for q in latest_news_list_f])
    outputv           = ', '.join([q.title for q in latest_news_list_v])
    outpute           = ', '.join([q.title for q in latest_news_list_e])
    outputs           = ', '.join([q.title for q in latest_news_list_s])
    return HttpResponse(outputf +'<br>'+ outputv +'<br>'+ outpute +'<br>'+ outputs)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    
def home(request):
    test = ws()    
    latest_news_list_T = test.getNews_technology()
    latest_news_list_S = test.getNews_Sport()
    latest_news_list_P = test.getNews_Political()
    latest_news_list_E = test.getNews_Economic()
    print('ok')

    context = {'latest_news_list_E': latest_news_list_E , 'latest_news_list_T': latest_news_list_T, 'latest_news_list_S': latest_news_list_S, 'latest_news_list_P': latest_news_list_P }
    return render(request, 'onlinenews/index.html', context)
    #outputT           = '<br> '.join([tag_a(q)for q in latest_news_list_T])
    #outputE           = '<br> '.join([tag_a(q)for q in latest_news_list_E])
    #outputS           = '<br> '.join([tag_a(q)for q in latest_news_list_S])
    #outputP           = '<br> '.join([tag_a(q)for q in latest_news_list_P])
    #OUT = '%s <hr> %s <hr> %s <hr> %s'%(outputT,outputE,outputS,outputP)
    #return HttpResponse(OUT)
    


