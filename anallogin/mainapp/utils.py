from telethon import TelegramClient
import requests


async def send_request_phone(client: TelegramClient, phone: str):
    await client.connect()
    sent = await client.send_code_request(phone=phone)

    phone_hash = sent.phone_code_hash

    with open('session.txt', 'w') as f:
        f.write(client.session.save())

    return phone_hash


async def send_sign_in(client: TelegramClient, request_post):
    await client.connect()
    sent = await client.sign_in(phone=request_post['phone'][0], code=request_post['code'][0], phone_code_hash=request_post['phone_code_hash'][0])
    print(sent)
    url = 'api url'
    requests.post(url, params={'session': client.session.save()})
