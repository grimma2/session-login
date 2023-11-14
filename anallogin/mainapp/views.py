import os
from telethon import TelegramClient
from telethon.sessions import StringSession

from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import PhoneForm, CodeForm
from .utils import send_request_phone, send_sign_in


class EnterPhone(View):

    def get(self, request):
        form = PhoneForm()
        return render(request, 'mainapp/enter_phone.html', context={'form': form})

    def post(self, request):
        form = PhoneForm(**request.POST)

        if form.is_valid():
            client = TelegramClient(StringSession(), os.environ['API_ID'], os.environ['API_HASH'])
            with client:
                client.loop.run_until_complete(send_request_phone(client=client, phone=form.cleaned_data['phone']))

            return redirect('mainapp:enter_code')
        else:
            return render(request, 'mainapp/enter_phone.html', context={'form': form})


class EnterCode(View):

    def get(self, request):
        form = CodeForm()
        return render(request, 'mainapp/enter_code.html', context={'form': form})

    def post(self, request):
        form = CodeForm(code=request.POST['code'])

        if form.is_valid():
            client = TelegramClient(StringSession(open('session.txt').read()), os.environ['API_ID'], os.environ['API_HASH'])
            with client:
                client.loop.run_until_complete(send_sign_in(**request.POST, client=client))
        else:
            render(request, 'mainapp/enter_code.html', context={'form': form})
