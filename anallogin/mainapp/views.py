import os
from telethon import TelegramClient
from telethon.sessions import StringSession
import asyncio

from django.shortcuts import render, redirect
from django.views.generic.base import View

from .forms import PhoneForm, CodeForm
from .utils import send_request_phone, send_sign_in


client = TelegramClient(StringSession(), os.environ['API_ID'], os.environ['API_HASH'])

class EnterPhone(View):

    def get(self, request):
        form = PhoneForm()
        return render(request, 'mainapp/enter_phone.html', context={'form': form})

    def post(self, request):
        print(request.POST)
        form = PhoneForm(request.POST)

        if form.is_valid():
            phone = form.cleaned_data['phone']
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            sent = loop.run_until_complete(send_request_phone(client=client, phone=phone))
            request.session['phone_code_hash'] = sent
            request.session['phone'] = phone

            return redirect('mainapp:enter_code')
        else:
            return render(request, 'mainapp/enter_phone.html', context={'form': form})


class EnterCode(View):

    def get(self, request):
        form = CodeForm()
        return render(request, 'mainapp/enter_code.html', context={'form': form})

    def post(self, request):
        form = CodeForm({'code': request.POST['code'][0]})
        print(request.POST)

        if form.is_valid():
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(send_sign_in(request_post=request.POST, client=client))
        else:
            render(request, 'mainapp/enter_code.html', context={'form': form})
