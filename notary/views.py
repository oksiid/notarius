from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.contrib import messages
# Create your views here.

def index(request):

    return render(request, 'index.html')

def zapis(request):
    if request.method == 'POST':
        messages.add_message(request, messages.INFO, 'Hello world.')

        text=f'Дата и Время: {request.POST["date"]} {request.POST["time"]} \n' \
             f'Имя: {request.POST["name"]} \n' \
             f'Телефон: {request.POST["phone"]} \n' \
             f'email: {request.POST["email"]} \n' \
             f'Пр-ст: {request.POST["prav_status"]} \n' \
             f'Нот-дейст: {request.POST["notary_action"]} \n' \
             f'Коммент: {request.POST["comment"]} \n'

        send_mail('amocrmНоваяЗапись', text, settings.EMAIL_HOST_USER, ['igor_kovalchuk_1976@mail.ru'])
        return HttpResponseRedirect(reverse('zapis'))
    return render(request, 'zapis.html')