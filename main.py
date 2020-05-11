import requests
import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
from sejong import *
from portalSejong import *
from oj import *
from exoj import *
from uis import *
from bb import *

server_status = [False,False,False,False,False,False]

if __name__ == '__main__':
    server_status[0] = sejong_init()
    server_status[1] = portal_init()
    server_status[2] = oj_init()
    server_status[3] = exoj_init()
    server_status[4] = uis_init()
    server_status[5] = bb_init()
    print(server_status)