
file = open("example.txt", 'rt', encoding='UTF8')

# 파일 내용 전체를 읽습니다.
content = file.read()
print(content)
print("------------------------------------")

# 파일 읽일 위치를 옮겨줌
file.seek(0)

# 파일에서 한 줄을 읽습니다.
line = file.readline()
print(line)
print("------------------------------------")

file.seek(0)

# 파일 읽일 위치를 옮겨줌
file.seek(0)
# 파일 전체를 읽고 각 줄을 리스트로 반환합니다.

lines = file.readlines()
print(lines)
print("------------------------------------")

file.close()  # 파일을 닫습니다.


# file = open("example.txt", "a")
#
# # 파일에 문자열을 씁니다.
# file.write("Hello, world!\n")
# file.write("This is an example file.\n")
#
# # 파일에 문자열의 리스트를 씁니다.
# lines = ["We will use it to demonstrate file writing in Python.\n",
#          "We can write multiple lines at once.\n"]
# file.writelines(lines)
#
# lines = file.readlines()
# print(lines)
# print("------------------------------------")

# file.close()  # 파일을 닫습니다.


# with 문은 파일을 열고 작업을 마치면 파일을 
# 자동으로 닫아줍니다.
# 예시
with open("example.txt", "r", encoding='UTF8') as file:
    # 파일을 다루는 코드
    content = file.read()
    print(content)
print("------------------------------------")

with open("example.txt", "r", encoding='UTF8') as file:
    # 파일 내용 전체를 읽습니다.
    content = file.read()
    print("read() 함수 예시:")
    print(content)

    # 파일에서 한 줄을 읽습니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    line = file.readline()
    print("readline() 함수 예시:")
    print(line)
    print("------------------------------------")

    # 파일 전체를 읽고 각 줄을 리스트로 반환합니다.
    file.seek(0)  # 파일 포인터를 처음으로 돌립니다.
    lines = file.readlines()
    print("\nreadlines() 함수 예시:")
    print(lines)
    print("------------------------------------")


"""
정규표현식(Regular Expression)
 문자열을 처리하는 패턴을 정의하는데 사용되는 형식 언어입니다. 
 정규표현식은 문자열의 검색(search)과 치환(replace) 작업에 사용됩니다.
 
 정규표현식의 메타 문자
. (마침표) : 임의의 문자 한 개를 의미합니다.
^ (캐럿) : 문자열의 시작을 의미합니다.
$ (달러) : 문자열의 끝을 의미합니다.
(별표) : 0개 이상의 문자를 의미합니다.
(더하기) : 1개 이상의 문자를 의미합니다.
? (물음표) : 0개 또는 1개의 문자를 의미합니다.

정규표현식의 리터럴
정규표현식의 리터럴은 문자 그대로를 의미합니다.
 예를 들어, "hello"는 정규표현식에서 "hello"라는 문자 그대로를 의미합니다.
"""

'''
문자열 매칭이란?
문자열 매칭(pattern matching)은 정규표현식을 사용하여 문자열 내에서 
특정한 패턴을 검색하는 과정입니다.
re.match() 함수
re.match() 함수는 문자열의 시작에서 패턴을 찾아서 반환합니다. 예를 들어, re.match(r"abc", "abcdef")는 "abc"와 매칭됩니다.
re.search() 함수
re.search() 함수는 문자열 내에서 패턴을 검색하여 반환합니다. 예를 들어, re.search(r"abc", "defabc")는 "abc"와 매칭됩니다.

r을 붙인 패턴 문자열은 Raw String(원시 문자열)로 
해석되어 백슬래시를 이스케이프 문자가 아니라 일반 문자로 처리됩니다.
'''
import re

# 문자열의 '시작' 부터 정규표현식과 매칭되는 패턴 찾기
pattern = r"python"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.match(pattern, string1)
match2 = re.match(pattern, string2)
match3 = re.match(pattern, string3) #  대문자라서 매칭을 못함

print(match1) # re.match 객체를 반환함

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")


print("---------------------------------------------------")
# search
import re

# 문자열 전체에서 정규표현식과 매칭되는 패턴 찾기
pattern = r"[pP]ython\W{1}\w{1,2}"
string1 = "python is easy"
string2 = "I love python"
string3 = "Python is fun"

match1 = re.search(pattern, string1)
match2 = re.search(pattern, string2)
match3 = re.search(pattern, string3)

if match1:
    print("매칭된 문자열:", match1.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match2:
    print("매칭된 문자열:", match2.group())  # 매칭된 문자열: python
else:
    print("매칭되지 않음")

if match3:
    print("매칭된 문자열:", match3.group())
else:
    print("매칭되지 않음")


'''
문자열 추출이란?
문자열 추출은 정규표현식을 사용하여 문자열 내에서 특정한 패턴을 검색하고 추출하는 과정입니다.

re.findall() 함수
re.findall() 함수는 문자열 내에서 패턴과 매칭된 모든 부분을 리스트로 반환합니다.
예를 들어, re.findall("a", "abcdaaa")는 ['a', 'a', 'a', 'a']와 같은 리스트를 반환합니다.
'''
import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴 찾기
pattern = r"[\s\S.](\d+)"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

matches1 = re.findall(pattern, string1)
matches2 = re.findall(pattern, string2)
matches3 = re.findall(pattern, string3)

print(matches1)  # ['2', '3']
print(matches2)  # ['-1', '5']
print(matches3)  # ['12345678']

'''
문자열 치환이란?
문자열 치환은 정규표현식을 사용하여 문자열 내에서 특정한 패턴을 검색하고
 다른 문자열로 치환하는 과정입니다.

re.sub() 함수
re.sub() 함수는 문자열 내에서 패턴과 매칭된 부분을 다른 문자열로 치환합니다. 

re.sub(pattern, repl, string, count=0, flags=0)

pattern: 정규표현식 패턴
repl: 치환할 문자열 또는 치환 함수
string: 대상 문자열
count: 치환할 최대 개수 (생략 가능)
flags: 정규표현식 옵션 (생략 가능)
'''

import re

# 문자열에서 정규표현식과 매칭되는 모든 패턴을 다른 문자열로 대체하기
pattern = r"\d+"
string1 = "I have 2 apples and 3 oranges"
string2 = "The temperature is -1.5 degrees Celsius"
string3 = "The password is 12345678"

result1 = re.sub(pattern, "10", string1)
result2 = re.sub(pattern, "0", string2)
result3 = re.sub(pattern, "***", string3)

print(result1)  # I have 10 apples and 10 oranges
print(result2)  # The temperature is -0.0 degrees Celsius
print(result3)  # The password is ***

'''
그룹핑은소괄호(())로 표현하며, 그룹핑된 문자열은 ()안에 위치합니다. 
그룹핑된 문자열은 해당 그룹핑의 순서대로 1, 2, 3...과 같은 그룹핑 인덱스를 부여받습니다. 
유용한 상황
매칭된 패턴에서 특정 부분만 추출하고자 할 때
매칭된 패턴에서 특정 부분을 치환하고자 할 때

그룹핑 추출 예시
전화번호에서 지역번호와 나머지 번호를 각각 추출
'''
import re

phone_number = "010-1234-5678"
pattern = r"(\d{2,3})-(\d{3,4})-(\d{4})"
result = re.match(pattern, phone_number)

print(result.group())
print(result.group(1))
print(result.group(2))
print(result.group(3))

area_code = result.group(1)
phone_number_without_area_code = result.group(2) + "-" + result.group(3)

print(area_code)  # 010
print(phone_number_without_area_code)  # 1234-5678


# 그루핑 치환
import re

date = "2022-03-18"
pattern = r"(\d{4})-(\d{2})-(\d{2})"
result = re.sub(pattern, r"\2/\3/\1", date)

print(result)  # "03/18/2022"

# 그룹핑 이름 순서 바꾸기
import re

# 이름 순서 바꾸기
string = "Kim, Yuna"
pattern = r"(\w+),\s*(\w+)"
result = re.sub(pattern, r"\2 \1", string)
print(result)  # "Yuna Kim"


# 멀티라인
string = """Python is an interpreted language
It is dynamically typed
And it is easy to learn"""

import re

pattern = '^Python|typed$'
result = re.findall(pattern, string, re.MULTILINE)
print(result)  # ['Python', 'typed']



# 이메일 주소 예시
import re

def extract_email(string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, string)
    return emails


string = "John's email is john.doe123@example.com. Jane can be reached at jane@example.co.uk." \
         " myemail is " \
         "sdat234qd.0294@naver.com." \
         "another email is " \
         "donghov1118@kakao.com"

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']


#  메일 주소의 유효성 검증
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, email):
        return True
    else:
        return False

email1 = 'example@example.com'
email2 = 'example@example.co.kr'
email3 = 'example.example.com'
email4 = 'example@example.'
email5 = 'example@example'

print(is_valid_email(email1))  # True
print(is_valid_email(email2))  # True
print(is_valid_email(email3))  # False
print(is_valid_email(email4))  # False
print(is_valid_email(email5))  # False


# ip 추출 예제
import re

log_data = [
    '192.168.0.1 - - [21/Feb/2022:10:12:01 +0900] "GET /index.html HTTP/1.1" 200 2326',
    '192.168.0.2 - - [21/Feb/2022:10:12:02 +0900] "GET /images/banner.jpg HTTP/1.1" 200 6571',
    '192.168.0.3 - - [21/Feb/2022:10:12:03 +0900] "POST /login.php HTTP/1.1" 302 -',
    '192.168.0.4 - - [21/Feb/2022:10:12:04 +0900] "GET /favicon.ico HTTP/1.1" 404 209'
]

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

for log in log_data:
    ip = re.findall(ip_pattern, log)
    print(ip)



