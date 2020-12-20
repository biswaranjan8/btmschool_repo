from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from studentapp.models import registerModel
from studentapp.forms import rgdForm
import random


def student_list(request):
    std_list = registerModel.objects.all()
    return render(request, 'student/student_list.html', context={'std_list': std_list})


def captcha_submit(request):
    num = random.randrange(1121, 9899)
    global str_num
    str_num = str(num)
    # --Registration form---
    rgd_form = rgdForm()
    return render(request, 'student/register_form.html', {'rgd_form': rgd_form, 'str_num': str_num})


def submit(request):
    # registration form
    register = False
    if request.method == 'POST':
        rgd_form = rgdForm(request.POST)
        cap = request.POST.get("captcha")
        if str(cap) == str_num:
            rgd_form.save()
            register = True
        else:
            return HttpResponse("<h4>Please correct input captcha!!!</h4>")
    return render(request,'student/register_form.html', context={'register': register})

"""def get_ip(request):
    address = request.META.get('HTTP_X_FORWARED_FOR')

    if address:
        ip = address.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


ip = get_ip(request)
u = User(user=ip)"""
