# sejong.ac.kr 메인 페이지에서 태그 2개 


from bs4 import BeautifulSoup
import requests
from PIL import Image
from urllib.request import urlopen

import urllib.request

# sejong.ac.kr 메인 홈페이지 url

sejong = 'http://sejong.ac.kr/' 
url = requests.get(sejong).text
bs = BeautifulSoup(url,'html.parser') 
flag = [0,0]

# 이미지 배너
# iframe src 
# http://www.sejongpr.ac.kr/mainsejongnewspaperlistnew.do?pageId=1
def find_imgBanner():
    innerContent = bs.find(attrs={'src':'http://www.sejongpr.ac.kr/mainsejongnewspaperlistnew.do?pageId=1'})['src']
    
    if(innerContent != None):
        iframeContent = requests.get(innerContent).text
        bs2 = BeautifulSoup(iframeContent,'html.parser')

        # 이미지 주소로 접속하게 위해 기존 도메인에 img src 추가
        imgSrc = 'http://www.sejongpr.ac.kr' +  bs2.find('img')['src']

        # 해당 이미지 주소로 접근 후 res 체크
        res = urllib.request.urlopen(imgSrc)
        if(res.status==200):
            flag[0] = 1 
            print('Sejong response',res.status)   
        else:
            flag[0] = 0
            print('response : ' + res.status) 
    else:
        print('이미지 배너 iframe의 url이 옳지 않습니다.')

# 공지사항 배너 
# iframe src 
# http://board.sejong.ac.kr/boardmainlistnew.do
def find_postBanner():
    innerContent = bs.find(attrs={'src':'http://board.sejong.ac.kr/boardmainlistnew.do'})['src']
    
    if(innerContent != None):
        iframeContent = requests.get(innerContent).text
        bs2 = BeautifulSoup(iframeContent,'html.parser')

        postCheck = bs2.find(attrs = {'title':'공지 게시판 미리보기 리스트'}).text
        
        # postCheck 타입 => str
        if(postCheck == None):
            flag[1] = 0
            print('공지게시판에 리스트가 없습니다.')
        else:
            flag[1] = 1
    else:
        print('공지사항 iframe의 url이 옳지 않습니다.')

def healthCheck():
    if(flag[0] == 1 & flag[1] == 1):
        print('서버 on')    
        return True    
    elif(flag[0] == 0 & flag[1] == 1):
        print('서버 off\n이미지 배너 접근 실패')
        return False
    elif(flag[0] == 1 & flag[1] == 0):
        print('서버 off\n공지사항 배너 접근 실패')
        return False
    else: 
        print('서버 off\n이미지 배너 & 공지사항 배너 접근 실패')
        return False

def sejong_init():
    find_imgBanner()
    find_postBanner()    
    server_status = healthCheck()
    print('--------------------------\n')
    return server_status
