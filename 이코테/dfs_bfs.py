stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최 하단 원소부터 출력
print(stack[::-1]) # 최상단 부터 출력

from collections import deque

# queue 구현 deque 라이브러리
queue = deque()


queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7) # 5, 2, 3, 7
queue.popleft() # 2, 3, 7
queue.pop()   # 2, 3
queue.append(1)
queue.append(4)

print(queue)
queue.reverse()
print(queue)

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1 부터 n 까지 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n<= 1:
        return 1
    return n* factorial_recursive(n-1)

print('반복적으로 구현 : ' , factorial_iterative(5))
print('재귀적으로 구현 : ' , factorial_recursive(5))
    
    