from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('windows-size=1920x1080')
    options.add_argument('disable-gpu')
    gini = webdriver.Chrome('C:/Users/user/Desktop/Henry/NetCluster/chromedriver_win32/chromedriver.exe', options=options)
    gini.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908')

    # 셀렉터
    # 순위 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
    # 이름 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
    # 가수 : #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

    soup = BeautifulSoup(gini.page_source, 'html.parser')
    song = soup.select('#body-content > div.newest-list > div > table > tbody > tr.list')

    for unwanted in song
        unwanteds = unwanted.select_one('td.number > span')
    unwanted_rank_find = soup.find('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number > span')
    unwanted_rank_select = soup.select('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number > span')
    print(unwanted_rank_select)
    unwanted_rank_find.extract()

    # # 1등 노래 코드, 2등 노래 코드, ... 이런 식으로 나열되어 있다. 무조건 리스트.
    # # unwanted_rank.extract()
    print(soup)
    #
    #
    # song_text = song.text
    # print(song_text)
    # for rank in song && for unwated_rank in song:
    #     ranks = rank.select_one('td.number')

    # print(unwanted_rank)
    # print(song)
    #     print(ranks.text.strip())

    gini.quit()