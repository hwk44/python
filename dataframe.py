# DataFrame
import pandas as pd
import numpy as np
print("================================================")
# 데이터프레임 생성 방법 1: 딕셔너리를 이용한 데이터프레임 생성
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
print("df1")
print(df1)
print("================================================")


# 데이터프레임 생성 방법 2: 리스트를 이용한 데이터프레임 생성
data = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
df2 = pd.DataFrame(data, columns=['A', 'B', 'C'])

print("df2")
print(df2)
print("================================================")

# 데이터프레임 생성 방법 3: Numpy 배열을 이용한 데이터프레임 생성
arr = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print("df3")
print(df3)
print("================================================")

# 데이터프레임 생성 방법 4: 시리즈를 이용한 데이터프레임 생성
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
s3 = pd.Series([7, 8, 9])
df4 = pd.DataFrame({'A': s1, 'B': s2, 'C': s3})
print("df4")
print(df4)
print("================================================")
# 데이터프레임 생성 방법 5: 외부 데이터 파일을 이용한 데이터프레임 생성
df5 = pd.read_excel('시군구_출생_20230324104737.xlsx')
print(df5)
print("================================================")


# 시리즈 생성
data = [10, 20, 30, 40, 50]
index = ['a', 'b', 'c', 'd', 'e']
s = pd.Series(data, index=index)

# 시리즈 인덱싱
print(s['a'])  # 10
print(s[['a', 'c', 'e']])  # a    10, c    30, e    50
print(s[:3])  # a    10, b    20, c    30
print(s[s > 30])  # d    40, e    50
print("================================================")


# print(df5.head())            # 상위 5개 데이터 출력
# print(df5.tail())            # 하위 5개 데이터 출력
# print(df5.info())            # 데이터프레임 정보 출력
# print(df5.describe())        # 수치형 열의 기술 통계 정보 출력
# print(df5.columns)           # 열 이름 출력
# print(df5.index)             # 행 인덱스 출력
# print(df5.dtypes)            # 열의 데이터 타입 출력
# print(df5.shape)             # 데이터프레임의 크기 출력
# print(df5.isnull().sum())    # 결측치 개수 출력


# 데이터프레임 생성
data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']
}
df = pd.DataFrame(data)

# 열 선택 방법 1: 대괄호([])를 이용한 단일 열 선택
name_col = df['name']
print(name_col)
print("================================================")

# 열 선택 방법 2: 점(.)을 이용한 단일 열 선택
age_col = df.age
print(age_col)
print("================================================")

# 열 선택 방법 3: 대괄호([])를 이용한 복수 열 선택
name_age_col = df[['name', 'age']]
print(name_age_col)

# 열 선택 방법 4: loc[]를 이용한 열 선택 // 열이름을 알고 있을때
name_col = df.loc[:, 'name']
print(name_col)
print("================================================")

# 열 선택 방법 5: iloc[]를 이용한 열 선택 // 열이름을 잘 모를때
name_age_col = df.iloc[:, [0, 1]]
print(name_age_col)
print("================================================")

a= df5.loc[:, '서울특별시']
print(a)
print("================================================")



# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 행 선택 방법 1: 대괄호([])를 이용한 단일 행 선택
row_0 = df.iloc[0]
print(row_0)
print("================================================")

# 행 선택 방법 2: loc[]를 이용한 단일 행 선택
row_1 = df.loc[1]
print(row_1)
print("================================================")

# 행 선택 방법 3: iloc[]를 이용한 복수 행 선택
rows_1_3 = df.iloc[[1, 3]]
print(rows_1_3)
print("================================================")

# 행 선택 방법 4: loc[]를 이용한 복수 행 선택
rows_2_4 = df.loc[[2, 4]]
print(rows_2_4)
print("================================================")

sub_df = df.loc[df['age'] >= 30]
print(sub_df)
print("================================================")

# 행 선택 방법 5: 슬라이싱을 이용한 범위 지정
rows_1_3 = df[1:4]
print(rows_1_3)


# 행 선택 방법 6: query()를 이용한 조건에 따른 행 선택
rows_age_over_30 = df.query('age > 30')
print(rows_age_over_30)
print("================================================")




# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 부분 데이터 선택 방법 1: loc[]를 이용한 조건에 따른 선택
sub_df_1 = df.loc[df['age'] > 30, ['name', 'city']]
print("=====================sub_df_1===========================")
print(sub_df_1)

# 부분 데이터 선택 방법 2: query()를 이용한 조건에 따른 선택
sub_df_2 = df.query("age > 30")[['name', 'city']]
print("=====================sub_df_2===========================")
print(sub_df_2)

# 부분 데이터 선택 방법 3: 슬라이싱을 이용한 범위 지정
sub_df_3 = df.iloc[1:3, 1:3]
print("=====================sub_df_3===========================")
print(sub_df_3)


# 부분 데이터 선택 방법 4: iloc[]를 이용한 인덱스 지정
sub_df_4 = df.iloc[[1, 3], [0, 2]]
print("=====================sub_df_4===========================")
print(sub_df_4)


# 부분 데이터 선택 방법 5: 조건에 따른 선택 후 열 지정
sub_df_5 = df[df['age'] > 30][['name', 'city']]
print("=====================sub_df_5===========================")

print(sub_df_5)
# 부분 데이터 선택 방법 6: at[]을 이용한 특정 위치 선택
val = df.at[1, 'age']
print("=====================sub_df_6===========================")
print(val)




''' dataframe 연산'''
data1 = {'A': [1, 2, 3], 'B': [4, 5, 10], 'C': [7, 8, 9]}
data2 = {'A': [9, 8, 7], 'B': [6, 5, 4], 'C': [3, 2, 1]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print("=====================df1===========================")
print(df1)
# 기본 연산
print("=====================더하기 연산===========================")
print(df1 + df2)
# 결과:
#    A  B  C
# 0 10 10 10
# 1 10 10 10
# 2 10 10 10

# 집계 함수
print("=====================df1.(mean) 한 행의 ===========================")
print(df1.mean()) # 결과: A    2.0, B    5.0, C    8.0, dtype: float64

print("=====================df1.mean(axis=1) 컬럼들의 평균===========================")
print(df1.mean(axis=1)) # 결과: 0    4.0, 1    5.0, 2    6.0, dtype: float64


# 예제 데이터
data = {'A': [1, np.nan, 3], 'B': [4, 5, np.nan], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

print("=========data 확인=========")
print(df)

# 결측치 확인

print("=========결측치 확인=========")
print(df.isnull())
# 결과:
#        A      B      C
# 0  False  False  False
# 1   True  False  False
# 2  False   True  False

# 결측치 대체
filled_df = df.fillna(0)
print("=========결측치 대체=========")
print(filled_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7
# 1  0.0  5.0  8
# 2  3.0  0.0  9

# 결측치 제거
dropped_df = df.dropna()
print("=========결측치 행 제거=========")
print(dropped_df)
# 결과:
#      A    B  C
# 0  1.0  4.0  7


# 예제 데이터
data = {'A': [1, 2, 2], 'B': [4, 5, 5], 'C': [7, 8, 8]}
df = pd.DataFrame(data)
print("=========data 확인=========")
print(df)
'''
   A  B  C
0  1  4  7
1  2  5  8
2  2  5  8
'''
# 중복 확인
print("=========중복 확인=========")
print(df.duplicated())
# 결과:
# 0    False
# 1    False
# 2     True

# 중복 제거
print("=========중복 제거=========")
deduplicated_df = df.drop_duplicates()
print(deduplicated_df)
# 결과:
#    A  B  C
# 0  1  4  7
# 1  2  5  8

print("=========================")
# 데이터프레임 생성
data = {'int_col': [1, 2, 3, 4, 5],
        'float_col': [1.1, 2.2, 3.3, 4.4, 5.5],
        'str_col': ['1', '2', '3', '4', '5'],
        'bool_col': [True, False, True, False, True],
        'category_col': ['a', 'b', 'c', 'a', 'b'],
        'date_col': ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']}

df = pd.DataFrame(data)
print(df.info())

# 열 데이터 형 변환
df['int_col'] = df['int_col'].astype(float)  # 정수형 -> 실수형
df['float_col'] = df['float_col'].astype(int)  # 실수형 -> 정수형
df['str_col'] = df['str_col'].astype(bool)  # 문자열 -> 불리언형
df['bool_col'] = df['bool_col'].astype(str)  # 불리언형 -> 문자열형
df['category_col'] = df['category_col'].astype('category')  # 문자열 -> 범주형
df['date_col'] = pd.to_datetime(df['date_col'])  # 문자열 -> 날짜/시간형

# 데이터프레임 정보 출력
print(df.dtypes)


# 데이터프레임 생성
data = {'gender': ['Male', 'Female', 'Male', 'Male', 'Female'],
        'age': [20, 30, 25, 35, 27],
        'city': ['Seoul', 'Busan', 'Seoul', 'Incheon', 'Seoul']}


df = pd.DataFrame(data)
print("============data 확인=============")
print(df)
# gender 열을 category 형으로 변환
df['gender'] = df['gender'].astype('category')

# city 열을 category 형으로 변환
df['city'] = df['city'].astype('category')

# 카테고리별 데이터 개수 확인
print(df['gender'].value_counts())
print(df['city'].value_counts())

# 카테고리별 통계량 확인
print(df.groupby('gender').mean(numeric_only=True))
print(df.groupby('city').mean(numeric_only=True))


# 샘플 데이터 생성
data = {
    'text': ['Hello, World!', 'Pandas is great', 'Python is awesome']
}

print("=================================")
df = pd.DataFrame(data)
print(df)

# 문자열 처리 작업
# 새로운 컬럼을 만들어 반환

print("==============str.lower()===================")
df['lower'] = df['text'].str.lower()  # 모든 문자를 소문자로 변환
print(df)

print("==============str.split()===================")
df['words'] = df['text'].str.split()  # 공백을 기준으로 단어 분할
print(df)

print("==============str.replace() 구두점, 기호 제거===================")
df['no_punctuation'] = df['text'].str.replace('[^\w\s]', '', regex=True)  # 구두점, 기호 제거
print(df)

df['word_count'] = df['text'].str.split().str.len()  # 단어 개수 계산

print(df.iloc[:, 1:])

