### 0327 강의

'''
NumPy
파이썬에서 다차원 배열을 처리하는 라이브러리입니다.
'''
# 임포트
import numpy as np

# 1차원 배열 생성
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # [1 2 3 4 5]

# 2차원 배열 생성
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# 배열 데이터 타입 지정
arr3 = np.array([1, 2, 3], dtype=float)
print(arr3)  # [1. 2. 3.]


arr = np.array([1, 2, 3, 4, 5])

# 슬라이싱은 [시작:끝:간격] 형식으로 사용
print(arr[1:4])  # [2 3 4]

# 다차원 배열의 슬라이싱
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0:2, 1:3])
'''
[[2 3]
 [5 6]]
'''

# 모든 행을 선택할 때는 ':'만 사용 가능
print(arr2d[:, 1])
'''
[2 5 8]
'''

'''
브로드캐스팅
브로드캐스팅은 NumPy에서 크기가 다른 배열 간의 연산을 가능하게 해주는 기능입니다. 브로드캐스팅은 작은 배열을 자동으로 확장하여 큰 배열에 맞추어 연산을 수행합니다.
'''
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6, 7])

# 브로드캐스팅을 통해 크기가 다른 배열 간 연산이 가능
# print(arr1 + arr2)  # [ 5  7  9 10] error

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 배열의 요소에 대해 적용되는 함수
print(np.add(arr1, arr2))  # [5 7 9]
print(np.multiply(arr1, arr2))  # [ 4 10 18]
print(np.power(arr1, arr2))  # [   1   32  729]

#===================================================
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# 배열 형태 변경
arr2d = arr.reshape((2, 4))
print(arr2d)

# 배열 구조 변경
arr2d_reshape = arr2d.reshape(4, 2)
print(arr2d_reshape)

# 배열 전치(Transpose)
arr2d_transpose = arr2d.T
print(arr2d_transpose)


# 통계 및 수학

# 정규 분포
arr1 = np.random.normal(0, 1, size=10)
print(arr1)
'''
[-1.03175853 -0.26330108  0.50114289  0.43128428  1.52632134
 -0.11669154 -0.38778772 -0.58322862  0.1852227  -1.12919514]
'''

# 균등 분포
arr2 = np.random.uniform(0, 1, size=10)
print(arr2)
'''
[0.3082703  0.59827088 0.61679035 0.3049514  0.10465949
 0.95647913 0.52484807 0.62345654 0.36863133 0.66491068]
'''

# 이항 분포
arr3 = np.random.binomial(10, 0.5, size=10)
print(arr3)
'''
[6 7 6 3 7 3 6 3 7 3]
'''

# 포아송 분포
arr4 = np.random.poisson(3, size=10)
print(arr4)
'''
[2 2 2 6 2 1 1 1 1 6]
'''
import pandas as pd

# Series 생성
# 리스트 사용
data = pd.Series([1, 2, 3, 4])
print(data)
# 결과:
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

# 문자열 인덱스 사용
data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(data)

# 딕셔너리 사용
data1 = {'a': 1, 'b': 2, 'c': 3 , 'd': 4}
s1 = pd.Series(data1)
print(s1)

# 결과:
# a    1
# b    2
# c    3
# d    4
# dtype: int64


