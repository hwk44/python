
import requests
from bs4 import BeautifulSoup
h = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win 64; x64)"
                    " AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/91.0.4472.77 Safari/537.36"}
url = "https://www.melon.com/chart/"
response = requests.get(url,headers= h)

soup = BeautifulSoup(response.text, "html.parser")
print(response.status_code)

# tbody = soup.select_one(".tbody")
tbody = soup.find_all('tr', {'class' : 'lst50'})

music = []
for tr in tbody:
#     print(tr.select('.rank').text) # 랭크
    rank = tr.find('span',{'class' : 'rank'}).text # 랭크
    title = tr.find('div', {'class' : 'ellipsis rank01'}).select_one('a').text # 제목
    singer = tr.find('div', {'class' : 'ellipsis rank02'}).select_one('a').text # 가수
    album = tr.find('div', {'class' : 'ellipsis rank03'}).select_one('a').text # 앨범
    music.append([rank, title, singer, album])
# print(music)

tbody = soup.find_all('tr', {'class' : 'lst100'})
for tr in tbody:
    rank = tr.find('span',{'class' : 'rank'}).text # 랭크
    title = tr.find('div', {'class' : 'ellipsis rank01'}).select_one('a').text # 제목
    singer = tr.find('div', {'class' : 'ellipsis rank02'}).select_one('a').text # 가수
    album = tr.find('div', {'class' : 'ellipsis rank03'}).select_one('a').text # 앨범
    music.append([rank, title, singer, album])
print(music)

import pandas as pd
# import csv
# f = open('music_info.csv', 'r', encoding='utf-8-sig')
# wr = csv.writer(f)
# for i in music:
#     wr.writerow(i)

df = pd.DataFrame(music, columns=['순위', '제목', '가수', '앨범명'])
df.to_csv('music_info.csv', index=False, encoding='utf-8-sig')

