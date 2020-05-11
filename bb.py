


import requests
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen

flag = [0]
def getTitle(url):
    try: 
        res = requests.get(url)
        res_code = res.status_code
    except:
        return None

    if int(res_code) == 200:
        print('Black Board response =',res_code)
        html = res.text
        bs = BeautifulSoup(html,'html.parser')
        return bs  
    else: 
        print('Black Board response =',res_code)
        return None

 
def healthCheck(bsObj):
    loginBtton = bsObj.find('button',{'id':'Portal_Button'})
    if(loginBtton != None):
        print('loginButton :',flag[0],'\n서버 ON')
        flag[0] = 1
        return True
    else:
        flag[0] = 0
        print('loginButton :',flag[0],'\n서버 OFF')
        return False
    
def bb_init():
    bsObj = getTitle('https://blackboard.sejong.ac.kr/')
    if(bsObj == None):
        print('Black Board 접속 실패')
        return False
    else:
        server_status = healthCheck(bsObj)
        print('--------------------------\n')
        return server_status