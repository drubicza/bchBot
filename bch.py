from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError
from time import sleep
import json, re, sys, os
try:
    import requests
    from bs4 import BeautifulSoup
except:
    print('\x1b[1;32m# \x1b[1;31mModul Requests Dan Bs4 Belum Terinstall\n\x1b[1;30m# \x1b[1;31minstall modul : pip install requests and pip install bs4')
    sys.exit()

banner = u'\x1b[0;35m\n    ___        __  ____   ___   ___   ___\n   / \\ \\      / / |___ \\ / _ \\ / _ \\ / _ \\ \n  / _ \\ \\ /\\ / /    __) | | | | | | | | | |\n / ___ \\ V  V /    / __/| |_| | |_| | |_| |\n/_/   \\_\\_/\\_/    |_____|\\___/ \\___/ \\___/\n===============================================\n[\u2022] Bot Bch click telegram auto skip captcha [\u2022]\n[\u2022] Subscribe yt AW 2000 [\u2022]\n'
print(banner)
if len(sys.argv) < 2:
    print('\n\n\n\x1b[1;32mUsage : python main.py +62')
    sys.exit(1)

def tunggu(x):
    sys.stdout.write('\r')
    sys.stdout.write('                                                               ')
    for remaining in range(x, 0, -1):
        sys.stdout.write('\r')
        sys.stdout.write('\x1b[1;30m#\x1b[1;0m{:2d} \x1b[1;32mseconds remaining'.format(remaining))
        sys.stdout.flush()
        sleep(1)


c = requests.Session()
ua = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36'}
api_id = 717425
api_hash = '322526d2c3350b1d3530de327cf08c07'
phone_number = sys.argv[1]
client = TelegramClient('session/' + phone_number, api_id, api_hash)
client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('\n\n\n\x1b[1;0mEnter Yout Code Code : '))
    except SessionPasswordNeededError:
        passw = input('\x1b[1;0mYour 2fa Password : ')
        me = client.start(phone_number, passw)

    myself = client.get_me()
    os.system('clear')
    print(banner)
    print('\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=\x1b[1;35m=')
    print(u'\x1b[1;32m[\u2022] Your name is =>', myself.first_name, u'\n\x1b[1;32m[\u2022] Enjoy And Happy miner !!\n\n')
    sleep(1)
    print('\x1b[1;31m++++++++++[ B ]++++++++++')
    sleep(1)
    print('\x1b[1;33m++++++++++[ C ]++++++++++')
    sleep(1)
    print('\x1b[1;32m++++++++++[ H ]++++++++++')
    sleep(1)
    print('\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+\x1b[1;35m+')
    print('\x1b[1;37mSending First command')
    try:
        channel_entity = client.get_entity('@BCH_clickbot')
        channel_username = '@BCH_clickbot'
        for i in range(5000000):
            sys.stdout.write('\r')
            sys.stdout.write('                                                              ')
            sys.stdout.write('\r')
            sys.stdout.write('\x1b[1;30m# \x1b[1;33mopen URL')
            sys.stdout.flush()
            client.send_message(entity=channel_entity, message=u'\U0001f5a5 Visit sites')
            sleep(3)
            posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            if posts.messages[0].message.find('Sorry, there are no new ads available') != -1:
                print(u'\n\x1b[1;32m[\u2022] \x1b[1;32miklan habis!\n[\u2022] Sorry, there are no new ads available \U0001f61f')
                sys.exit()
            else:
                try:
                    url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                    sys.stdout.write('\r')
                    sys.stdout.write(u'\x1b[1;35m[\u2022] \x1b[1;33mVisit ' + url)
                    sys.stdout.flush()
                    id = posts.messages[0].id
                    r = c.get(url, headers=ua, timeout=15, allow_redirects=True)
                    soup = BeautifulSoup(r.content, 'html.parser')
                    if soup.find('div', class_='g-recaptcha') is None:
                        pass
                    if soup.find('div', id='headbar') is None:
                        sleep(2)
                        posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        message = posts.messages[0].message
                        if posts.messages[0].message.find('You must stay') != -1 or posts.messages[0].message.find('Please stay on') != -1:
                            sec = re.findall('([\\d.]*\\d+)', message)
                            tunggu(int(sec[0]))
                            sleep(1)
                            posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                            messageres = posts.messages[1].message
                            sleep(1)
                            sys.stdout.write(u'\r\x1b[1;35m[\u2022] \x1b[1;32m' + messageres + '\n')
                    elif soup.find('div', id='headbar') is not None:
                        for dat in soup.find_all('div', class_='container-fluid'):
                            code = dat.get('data-code')
                            timer = dat.get('data-timer')
                            tokena = dat.get('data-token')
                            tunggu(int(timer))
                            r = c.post('https://dogeclick.com/reward', data={'code':code,  'token':tokena}, headers=ua, timeout=15, allow_redirects=True)
                            js = json.loads(r.text)
                            sys.stdout.write(u'\r\x1b[1;30m[\u2022] \x1b[1;32mYou earned ' + js['reward'] + ' BTC for visiting a site!\n')

                    else:
                        sys.stdout.write('\r')
                        sys.stdout.write('                                                                ')
                        sys.stdout.write('\r')
                        sys.stdout.write(u'\x1b[1;35m[\u2022] \x1b[1;31mCaptcha Detected')
                        sys.stdout.flush()
                        sleep(2)
                        client(GetBotCallbackAnswerRequest(channel_username,
                          id,
                          data=(posts.messages[0].reply_markup.rows[0].buttons[1].data)))
                        sys.stdout.write(u'\r\x1b[1;35m[\u2022] \x1b[1;31mSkipping chapta!      \n')
                        sleep(1)
                except:
                    sleep(1)
                    posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    message = posts.messages[0].message
                    if posts.messages[0].message.find('You must stay') != -1 or posts.messages[0].message.find('Please stay on') != -1:
                        sec = re.findall('([\\d.]*\\d+)', message)
                        tunggu(int(sec[0]))
                        sleep(1)
                        posts = client(GetHistoryRequest(peer=channel_entity, limit=2, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        messageres = posts.messages[1].message
                        sleep(2)
                        sys.stdout.write(u'\r\x1b[1;35m[\u2022] \x1b[1;32m' + messageres + '\n')

    finally:
        print(u'[\u2022] run again next day \U0001f60a')
        client.disconnect()
