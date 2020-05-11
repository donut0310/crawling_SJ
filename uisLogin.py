
import requests
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen

LOGIN_INFO = {
    'id': '16011088',
    'password': 'rla15964'
}

with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://portal.sejong.ac.kr/jsp/login/uisloginSSL.jsp', data=LOGIN_INFO)
    # 어떤 결과가 나올까요?
    print(login_req.status_code)
    
    html = s.get('http://uis.sejong.ac.kr/app/sys.Login.servj').text
    bs = BeautifulSoup(html,'html.parser')
    print(bs)

# /jsp/login/login_action.jsp

# http://uis.sejong.ac.kr/app/sys.Login.servj/jsp/login/login_action.jsp