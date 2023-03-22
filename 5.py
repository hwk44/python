
# 4장 뒷부분 내장 함수
'''
bin, oct, hex  int
bin(x), oct(x), hex(x)
10진 정수 x에 대한 2진수, 8진수, 16진수 문자열 반환
int(str, base=10)
문자열 str을 10진수로 변환
'''
print(bin(12))   #'0b1100'
print(int('123')) #123
print(int('1010', 2)) #10
'''
filter
filter(func,seq)
시퀀스의 각 요소에 대해 함수를 적용하여 결과가 True인 것만 모아서 리스트로 반환하는 함수
'''
# 리스트에서 짝수만 추출하는 예시
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력 결과: [2, 4, 6, 8, 10]

#round
num1 = 3.141592653589793238
num2 = 2.71828182845904523536

result1 = round(num1)     # 반올림하여 정수로 변환
result2 = round(num2, 3)  # 소수점 셋째자리까지 반올림

print(result1) # 출력 결과: 3
print(result2) # 출력 결과: 2.718

'''
ord
ord(ch)
ch에 대한 ASCII 코드 반환
ord('A')  65
'''
'''
repr
repr(obj)
obj를 문자열로 변환
repr(b'0011')  "b'0011'"
'''


'''
enumerate
enumerate(iterable,start=0)
주로 순서가 있는 자료형(리스트, 튜플 등)의 각 요소에 대해 인덱스와 값을 동시에 반환하는데 사용됩니다.
'''

colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(index, color)

''' eval
eval(expr,[globals[,locals]])
문자열로 표시된 파이썬 코드를 실행하고 결과를 반환
'''
result = eval('2 + 3 * 4')
print(result)  # 출력 결과: 14


'''
enumerate() 내장 함수를 이용하여 사용자가 입력한 문자열에서 'a' 
문자의 위치를 모두 찾아 출력하는 프로그램을 작성하라. 'a'가 없으면 "a가 없습니다'
라는 메시지를 출력하라.
'''
'''
s = str(input("문자열을 입력하세요"))

flag = 0

for i,ch in enumerate(s):
    if ch == 'a':
        print(i)
        flag=1

if flag == 0:
    print("a가 없습니다")
'''
'''
for st in s:
    print(st)
    if st == "a":
        print(st)
    else:
        print("'a'가 없습니다.")
'''

'''
두 수의 합(sum), 차(sub), 곱(mul), 나누기(div)를 수행하는 함수를 각각 정의하라.
 딕셔너리를 이용하여 사용자가 '1'을 입력하면 sum()을 호출하고, '2'를 입력하면 sub(), '3'을 입력하면 mul(),
  '4'를 입력하면 div() 함수를 호출하여 두 수의 연산을 수행하는 프로그램을 작성하라.
'''
'''
def sum(n,m):
    return n+m

def sub(n,m):
    return n-m

def mul(n,m):
    return n*m

def div(n,m):
    return n/m

table = {'1' : sum , '2' : sub , '3' : mul , '4' : div}

i = int(input("숫자를 입력하세요."))

func = table[str(i)]
print(func(2,3))
'''


'''
다음과 같이 구성되는 문자열을 구분 문자(&, =)로 분리하여
 딕셔너리로 반환하는 함수 작성
 예: 문자열 'led=on&motor=off&switch=off'이고 구분 문자가
  '&', '='일 때 {'led':'on', 'motor':'off', 'switch':off'} 반환.
  Hint: dict([['a','b'], ['c', 'd']])  {'a': 'b', 'c': 'd'}
'''
s = 'led=on&motor=off&switch=off'
print(s)

s1= s.split("&")
print(s1) # ['led=on', 'motor=off', 'switch=off']
s2 = list(map(lambda x : x.split("="),s1))
print(s2) # [['led', 'on'], ['motor', 'off'], ['switch', 'off']]
s2 = dict(s2) # 딕셔너리로 바꿈
print(s2) # {'led': 'on', 'motor': 'off', 'switch': 'off'}

temp = []
for item in s1:
    temp.append(item.split('='))

print(temp) # [['led', 'on'], ['motor', 'off'], ['switch', 'off']]
print(dict(temp)) # {'led': 'on', 'motor': 'off', 'switch': 'off'}