import asyncio
from telethon import TelegramClient
from telethon import functions, types
import questionary

api_id = int(questionary.password('Api ID:').ask())
api_hash = questionary.password('Api hash:').ask()

client = TelegramClient('session_new', api_id, api_hash)
client.start()

print('Bot started')


async def main():
    telegram_list = open('telegram_db', 'r').readlines()
    for (i,telegram_channel) in enumerate(telegram_list):
        if "https://" in telegram_channel:
            telegram_channel = telegram_channel.split('/')[-1]
        elif '@' in telegram_channel:
            telegram_channel = telegram_channel[1:]

        print(telegram_channel)
        result = client(functions.account.ReportPeerRequest(
            peer=telegram_channel,
            reason=types.InputReportReasonSpam(),
            message='RUSSIAN PROPAGANDA AGAINST UKRAINE DURING RUSSIAN INVASION IN UKRAINE'
        ))
        print(result)
        await asyncio.sleep(0.2)
with client:
    client.loop.run_until_complete(main())

