from django.shortcuts import render
from .bsoup import webScraping as ws
        
                
def home(request):
    test = ws()    
    latest_news_list_T = test.getNews_technology()
    latest_news_list_S = test.getNews_Sport()
    latest_news_list_P = test.getNews_Political()
    latest_news_list_E = test.getNews_Economic()
    print('ok')
    context = {'latest_news_list_E': latest_news_list_E , 'latest_news_list_T': latest_news_list_T, 'latest_news_list_S': latest_news_list_S, 'latest_news_list_P': latest_news_list_P }
    return render(request, 'onlinenews/index.html', context)


