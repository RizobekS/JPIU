from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect

from .models import News


def index(request):
    # filter news based on date and language availability
    if request.LANGUAGE_CODE == 'en':
        news_home = News.objects.filter(english=True).order_by('-pk')
    elif request.LANGUAGE_CODE == 'ru':
        news_home = News.objects.filter(russian=True).order_by('-pk')
    else:
        news_home = News.objects.filter(uzbek=True).order_by('-pk')

    return render(request, template_name="jpiu_app/home_page.html", context={'news_home': news_home})


def news(request):
    if request.LANGUAGE_CODE == 'en':
        list_news = News.objects.filter(english=True).order_by('-date')
    elif request.LANGUAGE_CODE == 'ru':
        list_news = News.objects.filter(russian=True).order_by('-date')
    else:
        list_news = News.objects.filter(uzbek=True).order_by('-date')

    page = request.GET.get('page', 1)
    paginator = Paginator(list_news, 10)  # number of news in each page

    try:
        list_news = paginator.page(page)
    except PageNotAnInteger:
        list_news = paginator.page(1)
    except EmptyPage:
        list_news = paginator.page(paginator.num_pages)

    return render(request, 'jpiu_app/news.html', {'news': list_news})


def news_details(request, pk):
    detail = News.objects.get(pk=pk)
    if request.LANGUAGE_CODE == 'en' and not detail.english:
        return HttpResponseRedirect(f"/{request.LANGUAGE_CODE}/news/")
    elif request.LANGUAGE_CODE == 'uz' and not detail.uzbek:
        return HttpResponseRedirect(f"/{request.LANGUAGE_CODE}/news/")
    elif request.LANGUAGE_CODE == 'ru' and not detail.russian:
        return HttpResponseRedirect(f"/{request.LANGUAGE_CODE}/news/")

    # increment views number by one every request
    detail.views += 1
    detail.save()

    return render(request, "jpiu_app/news_details.html", {'detail': detail})


def our_projects(request):
    return render(request, template_name="jpiu_app/our-projects.html")

