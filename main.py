import asyncio
import random
import pymongo
import os
import datetime

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon import functions, types

load_dotenv()

if os.getenv('MONGO_HOST'):
    mongoHost = os.getenv('MONGO_HOST')
else:
    mongoHost = '127.0.0.1'

myClient = pymongo.MongoClient(
    f"mongodb://{mongoHost}:27017/")

db = myClient["telegram_report_bot_ua"]

channelsCollection = db['channels']

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

client = TelegramClient('session_new', API_ID, API_HASH)
client.start()

print('Bot started')


async def fillDB():
    print('Fill Db started')

    telegram_list = open('telegram_db', 'r').readlines()

    for (i, telegram_channel) in enumerate(telegram_list):
        if "https://" in telegram_channel:
            telegram_channel = telegram_channel.split('/')[-1]
        elif '@' in telegram_channel:
            telegram_channel = telegram_channel[1:]
        try:
            telegram_channel = telegram_channel.split('\n')[0]
            splittedWithPriority = telegram_channel.split('|')

            if len(splittedWithPriority) == 1:
                name = splittedWithPriority[0]
            elif len(splittedWithPriority) == 2:
                name = splittedWithPriority[0]
                priority = int(splittedWithPriority[1])

            if not priority:
                priority = 0

            isInDb = channelsCollection.find_one({"name": name})

            if not isInDb:
                channelsCollection.insert_one({
                    "name": name,
                    "priority": priority,
                    "usageCount": 0,
                    "lastUsage": None,
                })

        except ValueError:
            print("Channel not found")


async def main():
    await fillDB()
    await runBot()


async def runBot():
    channels = channelsCollection.aggregate([{"$match": {}}, {"$sort": {
        "lastUsage": 1,
        "priority": -1,
    }}])

    for (i, telegram_channel) in enumerate(channels):
        try:
            message = 'Propaganda of the war in Ukraine. Propaganda of the murder of Ukrainians and Ukrainian soldiers.' + \
                str(random.random())

            result = await client(functions.account.ReportPeerRequest(
                peer=telegram_channel["name"],
                reason=types.InputReportReasonSpam(),
                message=message)
            )
            print(result)

            updateObject = {
                "$set": {
                    "lastUsage": datetime.datetime.now(),
                },
                "$inc": {
                    "usageCount": 1
                }
            }

            channelsCollection.update_one(
                {"_id": telegram_channel["_id"]}, updateObject)

        except ValueError:
            print("Channel not found")
        await asyncio.sleep(10 + 2 * random.random())
with client:
    client.loop.run_until_complete(main())
