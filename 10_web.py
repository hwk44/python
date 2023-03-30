import requests
from bs4 import BeautifulSoup

url = "https://www.hani.co.kr/arti/list.html?sec=news&subsec=politics"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
# titles = soup.find_all("h4", class_="article-title")
titles = soup.find_all("p", class_="article-prologue")


# titles = soup.find_all("img")
# h4 태그 중에 class 명이 article-title인 것을 가져옴 리스트 형태로
# for title in titles:
#     print(title.text.strip())

from bs4 import BeautifulSoup

html = '''
<html>
<body>
<div class="menu">
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</div>
<div class="content">
    <h1>Hello, World!</h1>
    <p>This is an example of using Beautifulsoup.</p>
</div>
</body>
</html>
'''


'''
soup = BeautifulSoup(html, 'html.parser')

# find() 메서드 사용 예시
div_menu = soup.find('div', {'class': 'menu'})
print(div_menu)

div_menu = soup.find('div', {'class': 'menu'})
print(div_menu)
links = div_menu.find_all('a')

# find_all() 메서드 사용 예시
# links = soup.find_all('a')
for link in links:
    print(link.get('href')) # 태그 속성 가져옴
    # print(link.text) # 태그 속성 가져옴

from bs4 import BeautifulSoup


# select 메서드 클래스 를 가져옴
html = '''
'''
<html>
<body>
<div class="menu">
    <ul>
        <li><a href="/home">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</div>
<div class="content">
    <h1>Hello, World!</h1>
    <p>This is an example of using Beautifulsoup.</p>
</div>
</body>
</html>
'''
'''
soup = BeautifulSoup(html, 'html.parser')

# CSS 선택자를 이용하여 태그 선택하기
menu = soup.select('.menu')
for m in menu:
    print(m)

# 복합 CSS 선택자를 이용하여 태그 선택하기
links = soup.select('div.menu a')
for link in links:
    print(link.get('href'))

'''
import requests
from bs4 import BeautifulSoup

url = 'https://movie.daum.net/ranking/reservation'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

ol = soup.select_one(".list_movieranking") # 클래스 명을 받아옴
li_list = ol.find_all('li')
print(li_list[0])

movie = []
for li in li_list:
    rank = li.select_one('.rank_num').text
    name = li.select_one('.link_txt').text
    see = li.select_one('.ico_see').text
    grade = li.select_one('.txt_grade').text
    num = li.select_one('.txt_num').text[:-1]
    mvdate = li.select_one('.txt_info > .txt_num').text
    # movie.setdefault(rank, name)
    movie.append([rank, name, see, grade, num, mvdate])
    # print(rank, name, see, grade, num, mvdate)
print(movie)

# 판다스 이용 csv 파일로 저장
import pandas as pd

df = pd.DataFrame(movie, columns=['순위', '제목', '관람가', "평점", '예매율', '개봉일'])
# 값을 여기 파이참에서 가져올경우 object 로 찍힘 전부 다 String 이라 비교 불가능

# df.to_csv('movie_info.csv', index=False, encoding='cp949') # 파일 저장

# 파일을 읽어와서 df로 만들면 int 로 알아서 변환
df = pd.read_csv('movie_info.csv', encoding='euc-kr')

# print(df.info())
print(df[df['평점'] > 8])

import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
# print(df.info())
df['개봉일'] = pd.to_datetime(df['개봉일'], format='%y.%m.%d')
print(df.info())

# 숫자 아닐때 에러 방지

df_weekly = df.resample('W', on='개봉일').mean(numeric_only=True)
print(df_weekly)
