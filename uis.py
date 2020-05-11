
import requests

from bs4 import BeautifulSoup

flag = [0,0]

def getTitle(url):
    try: 
        res = requests.get(url)
        res_code = res.status_code
    except:
        return None

    if int(res_code) == 200:
        print('UIS response =',res_code)
        html = res.text
        bs = BeautifulSoup(html,'html.parser')
        return bs  
    else: 
        print('UIS response =',res_code)
        return None


def healthCheck(bsObj):
    id = (bsObj.find('input',{'id':'id'}))
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

def uis_init():
    bsObj = getTitle('https://portal.sejong.ac.kr/jsp/login/uisloginSSL.jsp?rtUrl=uis.sejong.ac.kr/app/sys.Login.servj?strCommand=SSOLOGIN')
    if(bsObj == None):
        print('UIS 접속 실패')
        return False
    else:
        server_status = healthCheck(bsObj)
        print('--------------------------\n')
        return server_status