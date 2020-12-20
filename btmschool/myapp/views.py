from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import imagefiled, newspage
from .forms import signupForm, galleryform, newsform
from django.db.models import Q
import datetime


# Create your views here.

def homeViews(request):
    date_time = datetime.datetime.now()
    h = int(date_time.strftime('%H'))
    if 12 > h:
        msg = "Good Morning"
    elif 16 > h:
        msg = "Good Afternoon"
    elif 21 > h:
        msg = "Good Evening"
    else:
        msg = "Good Night"
    return render(request, 'myschool/home.html', context={'date_time': date_time, 'msg': msg})


def about(request):
    return render(request, 'myschool/about.html')


def news(request):
    daily_news = newspage.objects.order_by('id').reverse()
    pag = Paginator(daily_news, 3, orphans=1)
    page_number = request.GET.get('page')
    page_news_object = pag.get_page(page_number)
    return render(request, 'myschool/news.html', context={'page_news_object': page_news_object})


def administratorView(request):
    gallery = galleryform()
    if request.method == "POST":
        gallery = galleryform(data=request.POST, files=request.FILES)
        if gallery.is_valid():
            gallery.save()
            return redirect("/administrator")

    news = newsform()
    if request.method == "POST":
        news = newsform(data=request.POST, files=request.FILES)
        if news.is_valid():
            news.save()
            return redirect("/administrator")
    return render(request, 'myschool/administrator.html', context={'gallery': gallery, 'news': news})


def gallery(request):
    img = imagefiled.objects.all()
    return render(request, 'myschool/gallery.html', context={'img': img})


def gallery_edit(request):
    edit_img = imagefiled.objects.all()
    context = {'edit_img': edit_img}
    return render(request, 'myschool/gallery_edit.html', context)


def delete_gallery_view(request, id):
    dlt = imagefiled.objects.get(id=id)
    dlt.delete()
    return redirect('/gallery_edit')


def update_gallery_view(request, id):
    update_gallery = imagefiled.objects.get(id=id)
    if request.method == "POST":
        form = galleryform(request.POST, instance=update_gallery, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/gallery_edit')
    return render(request, 'myschool/update_gallery.html', context={'update_gallery': update_gallery})


class event_views(TemplateView):
    template_name = 'myschool/events.html'


# Sigh Up form.
def signup(request):
    signupform = signupForm()
    if request.method == 'POST':
        signupform = signupForm(request.POST)
        if signupform.is_valid():
            user = signupform.save()
            user.set_password(user.password)
            user.save()
            return redirect('/accounts/login')
    return render(request, 'registration/sign_up.html', {'signupform': signupform})


# Administrator logout..
def logout_views(request):
    return render(request, 'registration/logout.html')


# Search engine.
def search_views(request):
    query = request.GET['query']
    news = newspage.objects.filter(Q(title__icontains=query) | Q(body__icontains=query))
    context = {'news': news, 'query': query}
    return render(request, 'myschool/search.html', context)
