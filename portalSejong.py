import requests
import urllib.request

from urllib.request import urlopen
from bs4 import BeautifulSoup

flag = [0,0]

def getTitle(url):
    res = urllib.request.urlopen(url)
    print('Portal Sejong response =',res.status)
    
    if res.status != 200: return None
    else: 
        html = requests.get(url).text
        bs = BeautifulSoup(html,'html.parser')
        return bs  

def healthCheck(bsObj):
    id = bsObj.find('input',{'id':'id'})
    if(id != None):
        flag[0] = 1
    else: flag[0] = 0
    
    pw = (bsObj.find('input',{'id':'password'}))
    if(pw != None):
        flag[1] = 1
    else:
        flag[1] = 0

    if(flag[0] == 1 and flag[1] == 1):
        print('id 칸 :',flag[0],'\npw 칸 :',flag[1],'\n서버 ON')
        return True
    else: 
        print('id 칸 :',flag[0],'\npw 칸 :',flag[1],',\n서버 OFF')
        return False
        
def portal_init():
    bsObj = getTitle('https://portal.sejong.ac.kr/jsp/login/loginSSL.jsp')
    if(bsObj == None):
        print('url접속 실패')
        return False
    else:
        server_status = healthCheck(bsObj)
        print('--------------------------\n')
        return server_status