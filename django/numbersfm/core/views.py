from django.shortcuts import render
from news.models import NewsPost


def home(request):
    return render(request, 'home.html', {
            'news_post_list': NewsPost.objects.published()[:10]
            })
             
