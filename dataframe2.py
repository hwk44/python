import pandas as pd

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)

# 열 추가 방법 1: 기존 열을 이용하여 새로운 열 추가
df['age2'] = df['age'] + 1

# 열 추가 방법 2: insert() 메소드를 이용하여 특정 위치에 열 추가
df.insert(loc=2, column='gender', value=['F', 'M', 'M', 'M', 'F'])

# 열 추가 방법 3: assign() 메소드를 이용하여 여러 개의 열 한 번에 추가
df = df.assign(age3=[26, 31, 36, 41, 46], height=[160, 170, 180, 175, 165])

# 출력
print("=================df 확인=====================")
print(df)

# 행 추가 방법 1: append() 메소드를 이용하여 단일 행 추가
new_row = {'name': 'Frank', 'age': 50, 'city': 'Seoul'}
df = df.append(new_row, ignore_index=True)

# 행 추가 방법 2: append() 메소드를 이용하여 여러 행 추가
new_rows = [{'name': 'George', 'age': 22, 'city': 'Toronto'},
            {'name': 'Helen', 'age': 27, 'city': 'Sydney'}]
print("=================3명 추가=====================")
df = df.append(new_rows, ignore_index=True)

# 출력
print(df)

# 행 삭제 방법 1: drop() 메소드를 이용하여 단일 행 삭제
df = df.drop(0)

# 행 삭제 방법 2: drop() 메소드를 이용하여 여러 행 삭제
df = df.drop([1, 2])

# 열 삭제 방법 1: drop() 메소드를 이용하여 단일 열 삭제
df = df.drop('age', axis=1)

# 열 삭제 방법 2: drop() 메소드를 이용하여 여러 열 삭제
df = df.drop(['name', 'city'], axis=1)

# 출력
print("=================df 삭제=====================")
print(df)

''' 재정렬 '''

# 데이터프레임 생성
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [25, 30, 35, 40, 45],
        'city': ['New York', 'Paris', 'London', 'Berlin', 'Tokyo']}
df = pd.DataFrame(data)
print(df)

# 행 재정렬 방법 1: loc[]을 이용하여 행 순서 변경
print("===========4,3,2,1,0 순서로============")
df = df.loc[[4, 3, 2, 1, 0]]
print(df)

# 행 재정렬 방법 2: sort_values() 메소드를 이용하여 열 기준으로 정렬
df = df.sort_values('age', ascending=True)
print("===========age 열기준 정렬============")
print(df)

# 열 재정렬 방법 1: 열 이름 순서 변경
df = df[['city', 'name', 'age']]

# 열 재정렬 방법 2: 열 이름을 알파벳 순서로 정렬
df = df.reindex(sorted(df.columns), axis=1)

# 출력
print(df)

''' 데이터 병합 concat'''

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']})
print("=============df1============================")
print(df1)
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']})

print("=============df2============================")
print(df2)
'''
axis
0: 행방향
1: 열방향

ignore_index=True
인덱스가 0부터 시작하는 연속된 정수로 재설정
'''
result = pd.concat([df1, df2], axis=1, ignore_index=True)

print("=============concat=======================")
print(result)

''' Merge '''
left = pd.DataFrame({'key': ['K0', 'K1', 'K3'],
                     'A': ['A0', 'A1', 'A3'],
                     'B': ['B0', 'B1', 'B3']})
print("=============left=======================")
print(left)
right = pd.DataFrame({'key': ['K0', 'K2', 'K3'],
                      'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']})
print("=============right=======================")
print(right)

print("=============merge inner=======================")
result = pd.merge(left, right, on='key', how='inner')
print(result)

print("=============merge outer=======================")
result = pd.merge(left, right, on='key', how='outer')
print(result)

print("=============merge left=======================")
result = pd.merge(left, right, on='key', how='left')
print(result)

print("=============merge right=======================")
result = pd.merge(left, right, on='key', how='right')
print(result)

''' 그룹화 '''
# import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank'],
        'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
        'age': [25, 30, 35, 40, 45, 50],
        'score1': [80, 70, 85, 75, 90, 95],
        'score2': [85, 75, 90, 80, 95, 100],
        'city': ['Seoul', 'Busan', 'Seoul', 'Incheon', 'Jeju', 'Gwangju']
        }

df = pd.DataFrame(data)
print("=======df=======")
print(df)

# count
print("=======count=======")
print(df.groupby('gender')[['score1', 'score2']].count())

# size
print("=======size=======")
print(df.groupby('gender')[['score1', 'score2']].size())

# sum
print("=======sum=======")
print(df.groupby('gender')[['score1', 'score2']].sum())

# mean
print("=======mean=======")
print(df.groupby('gender')[['score1', 'score2']].mean())

# median
print("=======median=======")
print(df.groupby('gender')[['score1', 'score2']].median())

# min
print("=======min=======")
print(df.groupby('gender')[['score1', 'score2']].min())

# max
print("=======max=======")
print(df.groupby('gender')[['score1', 'score2']].max())

# std
print("=======std 표준편차=======")
print(df.groupby('gender')[['score1', 'score2']].std())

# var
print("=======var 분산=======")
print(df.groupby('gender')[['score1', 'score2']].var())

# sem
print("=======sem 표준오차=======")
print(df.groupby('gender')[['score1', 'score2']].sem())

# describe
print("=======describe 기술 통계=======")
print(df.groupby('gender')[['score1', 'score2']].describe())

''' 집계함수 사용 '''

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': [1, 2, 3, 4, 5, 6, 7, 8],
    'D': [10, 20, 30, 40, 50, 60, 70, 80]
})

print("===========df===========")
print(df)

result = df.groupby(['A', 'B']).agg({'C': 'count', 'D': ['sum', 'mean']})

print(result)

''' pivot table'''

df = pd.DataFrame({
    'Name': ['Alice', 'Alice', 'Bob', 'Bob', 'Alice', 'Alice', 'Bob', 'Bob'],
    'Date': ['Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2', 'Day 1', 'Day 2'],
    'Value': [10, 20, 15, 25, 30, 40, 35, 45]
})
print("===========df===========")
print(df)

result = df.pivot_table(values='Value', index='Name', columns='Date', aggfunc='mean')

print("===========피벗===========")
print(result)

# Date   Day 1  Day 2
# Name
# Alice     20     30
# Bob       25     35


# 매출 데이터 생성
data = {'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'],
        'Time': ['Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon', 'Morning', 'Afternoon'],
        'Sales': [100, 150, 200, 250, 300, 350, 400, 450]}
print("===========data===========")
df = pd.DataFrame(data)
print(df)

# 피벗테이블 생성
# result1 = pd.pivot_table(df, index='Region', columns='Time', values='Sales', aggfunc='sum')
# print("===========피벗테이블1  Sales ===========")
# print(result)

result2 = df.pivot_table(index='Region', columns='Time', values='Sales', aggfunc='sum')
print("===========피벗테이블  Sales ===========")
print(result)

# 나이 데이터 생성
ages = pd.DataFrame({'age': [22, 44, 65, 86, 27, 19, 51, 92, 33, 35, 38, 42, 14, 50, 78]})

# 연령대 구간 지정
bins = [0, 20, 40, 60, 80, 100]

# 연령대 카테고리 생성
age_categories = pd.cut(ages['age'], bins)
print(ages)

# 데이터프레임에 새로운 카테고리 열 추가
ages['age_categories'] = age_categories

# 결과 확인
print(ages)

result = pd.pivot_table(ages, index='age_categories', aggfunc='count')
print(result)

'''시계열 데이터 변환 pd.to_datetime()
문자열이나 다른 형식의 날짜와 시간 데이터를 datetime 형식으로 변환할 때 사용'''


data = {'date': ['2021-08-15 20:12:55', '2021-08-16', '2021-08-17'],
        'value': [100, 200, 150]}
df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
print("============date============")
print(df)
# print(df.info())
# Output:
#         date  value
# 0 2021-08-15    100
# 1 2021-08-16    200
# 2 2021-08-17    150


# 날짜 데이터 생성
df = pd.DataFrame({'date': ['2022년 01월 01일', '2022년 01월 02일', '2022년 01월 03일']})

# 날짜 데이터를 datetime 형식으로 변환
df['date'] = pd.to_datetime(df['date'], format='%Y년 %m월 %d일')

# 년, 월, 일 컬럼 추출
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day

# print(df.info())
print("============date============")
print(df)


data = {'date': ['2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02', '2022-01-01', '2022-01-02'],
        'location': ['서울', '서울', '부산', '부산', '대구', '대구'],
        'PM10': [50, 40, 45, 55, 60, 65],
        'PM2.5': [25, 20, 22, 28, 30, 35]}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

df_monthly = df.groupby('location').resample('D', on='date').mean(numeric_only=True)  # error
print(df_monthly)
