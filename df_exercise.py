import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('일별평균대기오염도_2022.csv', encoding="euc-kr")

# print(df.head())            # 상위 5개 데이터 출력
# print(df.tail())            # 하위 5개 데이터 출력
# print(df.info())            # 데이터프레임 정보 출력
# print(df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)

'''이중에서 측정일시, 미세먼지 농도, 초미세먼지 농도에 '''
# print(df[['측정일시', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']])
# print(df.iloc[ : , [0,1]])
# print(df.loc[ (df['미세먼지농도(㎍/㎥)'] >= 220 ) & (df['초미세먼지농도(㎍/㎥)'] >= 43) ,
#             ['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)'] ])

print(df.loc[(df['미세먼지농도(㎍/㎥)'] >= 30)][['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']])

sub_df = df.loc[df['미세먼지농도(㎍/㎥)'] > 220, ['측정소명', '미세먼지농도(㎍/㎥)']]
print(sub_df)


# print(df.query('측정소명 == "강남구"'))
# print(df.query('측정소명 == "강남구"'))


print(df.loc)
'''
print(df.head())            # 상위 5개 데이터 출력
print(df.tail())            # 하위 5개 데이터 출력
print(df.info())            # 데이터프레임 정보 출력
print(df.describe())        # 수치형 열의 기술 통계 정보 출력
print(df.columns)           # 열 이름 출력
print(df.index)             # 행 인덱스 출력
print(df.dtypes)            # 열의 데이터 타입 출력
print(df.shape)             # 데이터프레임의 크기 출력
print(df.isnull().sum())    # 결측치 개수 출력
'''


df2 = pd.read_csv('일별평균대기오염도_2022.csv', encoding="euc-kr")

df2 = df2[['측정일시', '측정소명', '미세먼지농도(㎍/㎥)', '초미세먼지농도(㎍/㎥)']]

df2 = df2.dropna()

df2['측정일시'] = pd.to_datetime(df2['측정일시'], format='%Y%m%d')
print(df2.head(20))
print(df2.info())


# 연도별 미세먼지와 초미세먼지 농도 평균 계산
df_monthly = df2.resample('M', on='측정일시').mean(numeric_only=True)

# 그래프 그리기
plt.plot(df_monthly.index.month, df_monthly['미세먼지농도(㎍/㎥)'], label='PM10')
plt.plot(df_monthly.index.month, df_monthly['초미세먼지농도(㎍/㎥)'], label='PM2.5')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Concentration')
plt.title('2022 Air Pollution Trend')
plt.show()