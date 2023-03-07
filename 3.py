
# 문자열 합치기
s1 = "Hello"
s2 = "world"
s3 = s1 + s2
print(s3)  # 출력: HelloWorld

# 문자열 반복
s4 = "Ha"
s5 = s4 * 3
print(s5)  # 출력: HaHaHa

# 문자열 길이 구하기
s6 = "Python is awesome"
print(len(s6))  # 출력: 17


# 문자열 인덱싱 예제 1
s = "Hello, World!"
print(s[0])   # 'H'
print(s[1])   # 'e'
print(s[-1])  # '!'

# 문자열 인덱싱 예제 2
s = "Python is a fun programming language!"
print(s[7])  # 'i'
print(s[11]) # 'f'
print(s[-12]) # 'm'

# 문자열 인덱싱 예제 3
s = "ABCDEFG"
print(s[1:4]) # 'BCD'
print(s[:3])  # 'ABC'
print(s[3:])  # 'DEFG'


# 문자열에서 홀수 번째 문자 추출하기
string = "abcdefghij"

result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]

print(result)  # 출력값: "acegi"

# 문자열 hello world에서 hlowrd 부분 문자열을 추출
string = "hello world"
substring = string[::2] # 2개씩 건너 뛰는 
print(substring)  # "hlowrd"

substring = string[::3] # 3개씩 건너 뛰는
print(substring)  # "hlwl"

#문자열을 뒤집는 예제
s = "Hello, world!"
reversed_s = s[::-1]
print(reversed_s)  # "!dlrow ,olleH" 인덱스가 1씩 감소

# 문자열 인덱스 범위를 벗어난 경우
s = "Hello"
# print(s[5])  # IndexError: string index out of range

# 인덱스가 올바른 범위 내에 있는지 확인해야 함
if len(s) > 5:
    print(s[5])  # ""
else:
    print("Index out of range")

# 문자열 슬라이스 범위를 벗어난 경우
s = "Hello"
print(s[1:10])  # "ello"


# 문자열 수정
s = "Hello"
# s[0] = "h"  # TypeError: 'str' object does not support item assignment

# 문자열은 불변(immutable)한 객체이므로, 새로운 문자열을 생성해야 함
s = "hello" + s[1:]
print(s)  # "hello"

s = "Hello, world!"
print(len(s))  # 13

s = "Hello, world!"
s_upper = s.upper()
print(s)  # "Hello, world!"
print(s_upper)  # "HELLO, WORLD!"

#print(s.upper)  # "HELLO, WORLD!"
#print("Hello, world!".upper)  

'''
isalnum(): 문자열이 알파벳과 숫자로만 이루어졌는지 여부를 반환합니다.
isalpha(): 문자열이 알파벳으로만 이루어졌는지 여부를 반환합니다.
isdecimal(): 문자열이 10진수 숫자로만 이루어졌는지 여부를 반환합니다.
isdigit(): 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
isidentifier(): 문자열이 파이썬 식별자로 사용 가능한지 여부를 반환합니다.
islower(): 문자열이 소문자로만 이루어졌는지 여부를 반환합니다.
isnumeric(): 문자열이 숫자로만 이루어졌는지 여부를 반환합니다.
isprintable(): 문자열이 출력 가능한지 여부를 반환합니다.
isspace(): 문자열이 공백 문자로만 이루어졌는지 여부를 반환합니다.
istitle(): 문자열이 제목 케이스로 이루어졌는지 여부를 반환합니다.
isupper(): 문자열이 대문자로만 이루어졌는지 여부를 반환합니다.
'''

'''
# 문자열 구성 파악 메소드 예시
print("hello123".isalnum())  # True
print("123".isalpha())  # False
print("123".isdecimal())  # True
print("123".isdigit())  # True
print("hello".isidentifier())  # True
print("hello".islower())  # True
print("123".isnumeric())  # True
print("Hello, World!".isprintable())  # True
print("   ".isspace())  # True
print("\t".isspace())  # True
print("Hello, World!".istitle())  # True
print("HELLO".isupper())  # True
'''

# 문자열 대소문자 변환 함수 예시
'''
print("hello, world!".upper())  # "HELLO, WORLD!"
print("HeLLo, wOrLd!".lower())  # "hello, world!"
print("hello, world!".capitalize())  # "Hello, world!"
print("hello, world!".title())  # "Hello, World!"
print("Hello, World!".swapcase())  # "hELLO, wORLD!"
'''


'''
문자열 찾기 함수
find(sub): 문자열에서 지정된 문자열(sub)을 찾아서 그 위치를 반환합니다.
        찾지 못한 경우에는 -1을 반환합니다.
rfind(sub): 문자열에서 지정된 문자열(sub)을 뒤에서부터 찾아서 그 위치를 반환합니다.
        찾지 못한 경우에는 -1을 반환합니다.
index(sub): 문자열에서 지정된 문자열(sub)을 찾아서 그 위치를 반환합니다.
        찾지 못한 경우에는 ValueError 예외가 발생합니다.
rindex(sub): 문자열에서 지정된 문자열(sub)을 뒤에서부터 찾아서 그 위치를 반환합니다.
        찾지 못한 경우에는 ValueError 예외가 발생합니다.
count(sub): 문자열에서 지정된 문자열(sub)이 몇 번 등장하는지 카운트하여 반환합니다.
'''

# 문자열 찾기 함수 예시
s = "hello, world!"

print(s.find("o"))  # 4
print(s.rfind("o"))  # 8
print(s.index("o"))  # 4
print(s.rindex("o"))  # 8
print(s.count("o"))  # 2

# 문자열 공백 삭제 및 변경 함수 예시
s = "  hello,   world!  "

print(s.strip())  # "hello,   world!"
print(s.lstrip())  # "hello,   world!  "
print(s.rstrip())  # "  hello,   world!"
print(s.replace("o", "0"))  # "  hell0,   w0rld!  "
print(s.replace("o", "0", 1))  # "  hell0,   w0rld!  "
print(s.strip().replace("o", "0", 1))  # "hell0,   world!  "


# split( )
# 문자열을 지정된 구분자(sep)로 나누어 "리스트" 로 반환합니다.
# sep 인자를 생략하면 공백을 구분자로 사용합니다.
# maxsplit 인자를 사용하여 나눌 횟수를 지정할 수 있습니다.

string = "hello world"
string_list = string.split()  # 기본값인 공백을 구분자로 사용
print(string_list)  # ['hello', 'world']

string = "apple,banana,grape"
string_list = string.split(",")  # 쉼표를 구분자로 사용
print(string_list)  # ['apple', 'banana', 'grape']


'''
splitlines( )
문자열을 개행 문자 또는 캐리지 리턴 문자 등을 기준으로 분리하여 리스트로 반환합니다.
join( )
문자열을 반복 가능한 객체의 요소들을 구분자로 연결하여 반환합니다.

'''
# 문자열 분리, 결합 함수 예시
s = "apple,banana,grape"

print(s.splitlines())  # ["apple", "banana", "grape"]
print(",".join(["apple", "banana", "grape"]))  # "apple,banana,grape"


# 문자열 정렬, 채우기 함수 예시
s = "hello"

print(s.center(10))  		# "  hello   "
print(s.center(10, "-"))    # "--hello---"
print(s.ljust(10))         	# "hello     "
print(s.ljust(10, "*"))  	# "hello*****"
print(s.rjust(10)) 			# "     hello"
print(s.rjust(10, "+"))  	# "+++++hello"
print("123".zfill(5))  		# "00123"

'''
s = str(input("문자열을 입력하세요."))
print(len(s)) # 문자열의 문자수를 출력하라
print(s*10)   #문자열을 10번 반복한 문자열을 출력하라
print(s[0])   #문자열의 첫 번째 문자를 출력하라
print(s[:3])  #문자열에서 처음 3문자를 출력하라
print(s[-3:])  #문자열에서 마지막 3문자를 출력하라
print(s[::-1])  #문자열의 문자를 거꾸로 출력하라
if len(s) > 6:  #문자열에 7번째 문자가 있으면 출력하고 없으면
    print(s[6]) #'문자가 없습니다'라는 메시지를 출력하라
else:
    print("문자가 없습니다.")
print(s[1:-1])  # 문자열에서 첫 번째 문자와 마지막 문자를 제거한 문자열을 출력하라
print(s.upper()) # 모두 대문자로 변경하여 출력하라
print(s.lower())  # 모두 소문자로 변경하여 출력하라
print(s.replace("a", "e")) #'a'를 'e'로 대체하여 출력하라
'''


'''
문자 'a'가 들어가는 단어를 키보드에서 입력 받아 첫 번째 줄에는
'a'까지의 문자열을 출력하고 두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.
Your word: Buffalo
Buffa
lo
'''
'''
s = str (input("문자열을입력하세요."))
print(s.find("a"))
print(s[0:s.find("a") +1])
print(s[s.find("a") + 1 :])
'''

'''
숫자를 문자열로 변화하는 방법은 str(num)을 이용한다.
str(12) -> '12'가 된다. 반대로 문자열을 숫자로 변환하려면
int(string)을 이용한다. int('12') -> 12가 된다.
이를 이용하여 1부터 1000까지의 숫자의 각 자리수의 합을 모두 구하라.
예를 들어 234 -> 2+3+4=9가 된다
[Hint]
sum = 0
for s in '234':
    sum += int(s)
'''

sum = 0;
for i in range(1,1001):
    st= str(i) # 정수를 문자열로 바꾼다.
    for s in st:
        sum+= int(s)
print(sum)




# 리스트
numbers = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie']

# 튜플
numbers = (1, 2, 3, 4, 5)
names = ('Alice', 'Bob', 'Charlie')

'''
리스트 컴프리헨션(List Comprehension)
'''
#1부터 10까지의 숫자 중에서 짝수만 포함하는 리스트를 생성
even_numbers = [num for num in range(1, 11) if num % 2 == 0]
print(even_numbers)  # 출력: [2, 4, 6, 8, 10]

# 리스트 내 모든 요소에 1을 더하는 예제
original_list = [1, 2, 3, 4, 5]
new_list = [num + 1 for num in original_list]
print(new_list)  # [2, 3, 4, 5, 6]

# 리스트 내 문자열의 길이를 구하는 예제
words = ['apple', 'banana', 'cherry', 'durian']
word_lengths = [len(word) for word in words]
print(word_lengths)  # [5, 6, 6, 6]

# 이터러블 객체를 만들고
my_list = [1, 2, 3, 4, 5]

# 이터러블 객체로 이터레이터 생성
my_iter = iter(my_list)

# 이터레이터를 사용하여 값을 출력
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3

'''
3명 이상 친구 이름 리스트를 작성하고 다음 내용을 프로그램하시오 
insert()로 맨 앞에 새로운 친구 추가
insert()로 3번째 위치에 새로운 친구 추가
append()로 마지막에 친구 추가

'''
friends = ["김유신", "이순신", "세종"]
print(friends)
friends.insert(0,"혁거세")
print(friends)
friends.insert(2, "조세호")
print(friends)
friends.append("박명수")
print(friends)


'''
리스트 [1, 2, 3]에 대해 다음과 같은 처리를 하라.
두 번째 요소를 17로 수정
리스트에 4, 5, 6을 추가
첫 번째 요소 제거
리스트를 요소 순서대로 배열하기
인덱스 3에 25넣기
'''
a = [1,2,3]
a[1] = 17
print(a)
a += [4,5,6] # 리스트에 4, 5, 6을 추가
print(a)
del a[0]
print(a)
a.sort() # 리스트를 요소 순서대로 배열하기
print(a)

a.insert(3,25) # 인덱스 3에 25넣기
print(a)

# 0~49까지의 수로 구성되는 리스트
li = [i for i in range(1,50)]
print(li)

# 1~50까지 수의 제곱으로 구성되는 리스트
li2 = [i**2 for i in range(1,51)]
print(li2)

'''
크기가 같은 두 개의 리스트 L, M을 생성하고
두 리스트의 각 요소 합으로 구성되는 새로운 리스트를 생성하라.
예를 들어 L=[1,2,3]이고 M=[4,5,6]이면 [5,7,9]인 리스트 생성
'''
L = [1, 2, 3]
M = [4, 5, 6]

LM = [L[i]+M[i] for i in range(0, len(L))]
print(LM)

"""사용자로부터 5개의 숫자를 문자열로 입력 받아 각 숫자를
+로 연결한 문자열을 생성하라.
예를 들어 2, 5, 11, 33, 55를 입력하면 '2+5+11+33+55'를 생성하라.
"""
'''
s = ""
for i in range(1,6):
    st = str(input("숫자를 입력하세요."))
    s += st
    if i ==5:
        break
    s += "+"
print(s)

num_list = input("5개의 숫자를 입력하세요.(구분자 : 띄어쓰기) : ").split()
result = "+".join(num_list)
print(result)
'''

# 튜플
# 튜플 생성
my_tuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')

# 인덱싱
print(my_tuple[0])   # 'apple' 출력
print(my_tuple[-1])  # 'mango' 출력

# 슬라이싱
print(my_tuple[2:5])   # ('cherry', 'orange', 'kiwi') 출력
print(my_tuple[:4])    # ('apple', 'banana', 'cherry', 'orange') 출력
print(my_tuple[2:])    # ('cherry', 'orange', 'kiwi', 'melon', 'mango') 출력
print(my_tuple[::2])   # ('apple', 'cherry', 'kiwi', 'mango') 출력
print(my_tuple[::-1])  # ('mango', 'melon', 'kiwi', 'orange', 'cherry', 'banana', 'apple') 출력


# 튜플 언패킹 각 요소를 개별 변수로 할당 
my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

#튜플 언패킹을 이용해서 두 변수의 값을 교환
x = 1
y = 2
x, y = y, x
print(x)  # 2
print(y)  # 1


# 튜플을 리스트로 변환
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)

# 리스트를 튜플로 변환
my_list = [6, 7, 8, 9, 10]
my_tuple = tuple(my_list)
print(my_tuple)

# 형변환시 주의. 튜플 내부에 리스트가 있으면 값 변경  가능 
my_list = [1, 2, [3, 4]]
my_tuple = tuple(my_list)
print(my_tuple) # 출력 결과: (1, 2, [3, 4])

my_tuple[2][0] = 5
print(my_tuple) # 출력 결과: (1, 2, [5, 4])


def calculate(x, y):
    add = x + y
    subtract = x - y
    multiply = x * y
    divide = x / y
    return add, subtract, multiply, divide
result = calculate(10, 2)  #  결과: (12, 8, 20, 5.0)
print(calculate(10,2))
print(result)