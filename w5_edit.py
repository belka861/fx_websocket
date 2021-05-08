import websocket, requests,random
import time,sys,datetime
from phone_gen import PhoneNumber
from random_username.generate import generate_username
logfile='webscoket.log'
def _log(message):
#    fh=open(logfile,"a",encoding="cp1251")
    fh=open(logfile,"a")
    text=str(datetime.datetime.now())+" "+str(message)+"\r\n"
    print(text)
    fh.write(text)
    fh.close()
    return True

import requests

from transliterate import translit, get_available_language_codes
url = 'https://raw.githubusercontent.com/belka861/fx_message/main/phrases.txt'
r = requests.get(url, allow_redirects=True)
open('phrases.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_websocket/main/names_f.txt'
r = requests.get(url, allow_redirects=True)
open('names_f.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_websocket/main/countries.txt'
r = requests.get(url, allow_redirects=True)
open('countries.txt', 'wb').write(r.content)

url = 'https://raw.githubusercontent.com/belka861/fx_websocket/main/surnames_f.txt'
r = requests.get(url, allow_redirects=True)
open('surnames_f.txt', 'wb').write(r.content)

with open('nyse-listed.csv', 'r') as file:
    nyse = file.readlines()



#main logic

while True:
    with open('phrases.txt', 'r') as file:
        data = file.readlines()
#print(data)
    question=data[random.randint(1,len(data)-1)].replace('\n', '')
#    _log(question)

    with open('names_f.txt', 'r') as file:
        data = file.readlines()
    #print(data)
    name=data[random.randint(1,len(data)-1)].replace('\n', '')
#    _log(name)

    with open('surnames_f.txt', 'r') as file:
        data = file.readlines()
    #print(data)
    surname=data[random.randint(1,len(data)-1)].replace('\n', '')
#    _log(surname)
    tick=nyse[random.randint(1,len(nyse)-1)].replace('\n', '')
#    print (tick)
#    sys.exit()

    with open('countries.txt', 'r') as file:
        data = file.readlines()
#print(data)
    country=data[random.randint(1,len(data)-1)].replace('\n', '')
#    _log(country)


    ph=PhoneNumber(country)
    tn=ph.get_number(full=False)
    tnf=ph.get_number()
#    _log (tnf)
#sys.exit()
    t=(round(time.time()*1000))


    dice=random.choice([1,2,3])
    _log (dice)
    if (dice==1):
        final_name=name
    if (dice==2):
        final_name=name+" "+surname
    if (dice==3):
        final_name=surname+" "+name
#    sys.exit()
#    _log(final_name)


    dice=random.choice([1,2,3,4,5,6,7,8,9,20])
    if (dice==5):
        question="Мне аналитик посоветовал купить акции "+tick+" А ОНИ СЕГОДНЯ ОБВАЛИЛИСЬ! ВЕРНИТЕ МНЕ МОИ ДЕНЬГИ!!!"



    domains=['mail.ru','yandex.ru', 'rambler.ru', 'outlook.com', 'gmail.com', 'hotmail.com', 'list.ru', 'bk.ru', 'inbox.ru', 'internet.ru',  'yahoo.com', 'aol.com', 'e1.ru','inbox.lv', 'dino.lv','human.lv', 'fit.lv','sok.lv', 'eclub.lv', 'zohomail.com', 'protonmail.com', 'mail.com', 'usa.com', 'counsellor.com', 'cyberservices.com', 'protestant.com']
    password=""
    for i in range (1,7):
        password=password+random.choice('01234567890')

    username=generate_username(1)[0]+password
    username=translit(final_name, reversed=True).replace(" ", "_").replace("'","").lower()+password
#    print(username)
#    sys.exit()
    domain=random.choice(domains)
    email=username+"@"+domain
#    _log (email)
    _log (final_name+" "+tnf+" "+country+" "+email+" "+question)

#sys.exit()
    websocket.enableTrace(False)
    ws = websocket.WebSocket()
    ws.connect("wss://node231.jivosite.com/cometcn", origin="testing_websockets.com")

#    ws.connect("wss://node-eu1-b-1.jivosite.com/cometcn", origin="testing_websockets.com")

#wss://node-eu1-b-1.jivosite.com/cometcn

#test below

    ws.send('{"name":"startup","jv_widget_id":"KSPtF7hWOu","site_id":1576660,"current_page":{"title":"24xFOREX","url":"https://24xforex.com/"},"is_mobile":false,"visits_count":1,"page_visible":true,"chat_opened":true,"widget_version":"32.4.0","history":[{"url":"https://24xforex.com/","title":"24xFOREX","time":'+str(t)+'}],"new_utm":{"campaign":"(direct)","source":"(direct)"},"visitor_id":"f07d59bbc15f5547"}')
#                                                                                                                                                                                                                                                      1619908687848
    _log(ws.recv())
#time.sleep(1)
#ws.send('.')
#print(ws.recv())



    m='{"name":"introduction","client_name":"'+final_name+'","phone":"'+tnf+'","email":"'+email+'","description":null,"accept_eula":null}'
    _log(m)
    ws.send(m)
    m='{"name":"client_message","message":"'+question+'","private_id":"a2143b95-a0bd-7990-69cd-1a70f4235961"}'
    _log(m)
    ws.send(m)

#ws.send('{"name":"introduction","client_name":"'+final_name+'","phone":"'+tnf+'","email":"'+email+'","description":null,"accept_eula":null}')
#ws.send('{"name":"client_message","message":"'+question+'","private_id":"a2143b95-a0bd-7990-69cd-1a70f4235961"}')

    _log(ws.recv())
    _log(ws.recv())
    _log(ws.recv())
#print(ws.recv())
#print(ws.recv())
#    sys.exit()
    time.sleep(10)
    ws.close()

