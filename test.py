# import copy
#
# # Create a list with variable name a
# a = [1, 2, [3, 4]]
# b = copy.copy(a)
# b[1] = 0
# print(a)
# print(b)
#
# '''
# 리스트 컴프리헨션(List Comprehension)
# '''
# # 1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성
# even_numbers = [num for num in range(1, 11) if num % 2 == 0]
# print(even_numbers)  # 출력: [2, 4, 6, 8, 10]
#
# # 리스트 내 모든 요소에 1을 더하는 예제
# original_list = [1, 2, 3, 4, 5]
# new_list = [num + 1 for num in original_list]
# print(new_list)  # [2, 3, 4, 5, 6]
#
# # 리스트 내 문자열의 길이를 구하는 예제
# words = ['apple', 'banana', 'cherry', 'durian']
# word_lengths = [len(word) for word in words]
# print(word_lengths)  # [5, 6, 6, 6]
#
# # 이터러블 객체를 만들고
# my_list = [1, 2, 3, 4, 5]
#
# # 이터러블 객체로 이터레이터 생성
# my_iter = iter(my_list)
#
# # 이터레이터를 사용하여 값을 출력
# print(next(my_iter))  # 1
# print(next(my_iter))  # 2
# print(next(my_iter))  # 3
#
# # Create a tuple containing 5 numbers
# import statistics
#
# numbers = (3, 7, 2, 9, 5)
# # num_list = list(numbers)
# print(max(numbers))
# print(min(numbers))
# result = statistics.mean(numbers)
# print(result)
#
#
# def remove_vowels(s):
#     # implement your code
#     vowels = 'aeiou'
#     str_temp = ""
#     for ch in vowels:
#         str_temp = s.replace(ch, "")
#     return str_temp
#
# print(remove_vowels("apple"))
#
# s1 = "apple"
# vowels = ['a', 'e', 'i', 'o', 'u']
# # s2 = ""
# # s2 = s1.replace('p', "")
# # print(s2)
# str_temp = ""
# for ch in vowels:
#     str_temp = s1.replace(ch, "")
# print(str_temp)

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

df = pd.DataFrame(music, columns=['순위', '제목', '가수', '앨범명'])
df.to_csv('music_info.csv', index=False, encoding="UTF-8")

# print(tbody)
# print(tbody)
# print(tbody.select('.rank').text) # 랭크
# print(tbody.find('div', {'class' : 'ellipsis rank01'}).select_one('a').text) # 제목
# print(tbody.find('div', {'class' : 'ellipsis rank02'}).select_one('a').text) # 가수
# print(tbody.find('div', {'class' : 'ellipsis rank03'}).select_one('a').text) # 앨범
#
# print(tbody.select_one('.cnt').text) #

# print(tbody.select_one('.ellipsis rank01 > a').text)
# print(tbody.select_one('.rank').text)
# print(tbody.select_one('.rank').text)


# b = soup.select_one('.cnt')
# print(b)
# titles = soup.find_all('span', class_='rank')
# for title in titles:
#     print(title.text.strip())
# print(titles)

# for i in range(0,10)

# n = 7
# s = ""
# for i in range(1, 10):
#     # print(f"{n} x {i} = {n*i}")
#     s += f"{n} x {i} = {n*i}\n"
# print(s)