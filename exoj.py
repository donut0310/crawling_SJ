
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
        print('EX-OJ response =',res_code)
        html = res.text
        bs = BeautifulSoup(html,'html.parser')
        return bs  
    else: 
        print('EX-OJ response =',res_code)
        return None

             
def healthCheck(bsObj):
    head = (bsObj.find('div',{'class':'modal-header'})).find('h3')
    if(head != None):
        flag[0] = 1
    else: flag[0] = 0
    
    id = (bsObj.find('input',{'id':'id'}))
    if(id != None):
        flag[1] = 1
    else:
        flag[1] = 0
    
    if(flag[0] == 1 and flag[1] == 1):
        print('h3 Tag :',flag[0],'\nid 칸 :',flag[1],'\n서버 ON')
        return True
    else: 
        print('h3 Tag :',flag[0],'\nid 칸 :',flag[1],',\n서버 OFF')
        return False

def exoj_init():
    bsObj = getTitle('https://ex-oj.sejong.ac.kr/index.php/auth/login/')
    if(bsObj == None):
        print('EX-OJ 접속 실패')
        print('--------------------------\n')
        return False
    else:
        server_status = healthCheck(bsObj)
        print('--------------------------\n')
        return server_status
