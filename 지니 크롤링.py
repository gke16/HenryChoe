from pymongo import MongoClient
import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('windows-size=1920x1080')
    options.add_argument('disable-gpu')
    gini = webdriver.Chrome('C:/Users/user/Desktop/Henry/NetCluster/chromedriver_win32/chromedriver.exe', options=options)
    gini.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908')

    client = MongoClient('localhost', 27017)
    db = client.dbgini

    # 셀렉터
    # 순위 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    # 이름 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
    # 가수 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

    soup = BeautifulSoup(gini.page_source, 'html.parser')
    songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
    # print(song)

for song in songs:
    person = song.select_one('td > a.artist.ellipsis').text.strip()
    name = song.select_one('td > a.title.ellipsis').text.strip()
    unwanted_rank = song.select_one('td.number > span')
    unwanted_rank.extract()
    rank = song.select_one('td.number').text.strip()
    # print(rank, name, person)
    db.songRanking.insert_one({'rank': rank, 'song': name, 'artist': person})


gini.quit()