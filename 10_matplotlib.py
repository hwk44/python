import matplotlib.pyplot as plt
import numpy as np

'''선그래프'''
# x, y 데이터 생성
x = np.arange(0, 10, 0.01) # 점 찍는 함수
y = np.sin(x)

# 선 그래프 그리기
# plt.plot(x, y)

# 그래프 타이틀과 축 라벨 설정
# plt.title('Sine Wave')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markersize=2)

# 그래프 출력
# plt.show()


# 산점도

# x, y 데이터 생성
# x = np.random.rand(100)
# y = np.random.rand(100)

# 산점도 그리기
# plt.scatter(x, y)

# 그래프 타이틀과 축 라벨 설정
# plt.title('Scatter Plot')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)

# 그래프 출력
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 라인 스타일 변경 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed')
plt.plot(x, y2, linestyle='dashdot')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, linestyle='dashed', label='Sine')
plt.plot(x, y2, linestyle='dashdot', label='Cosine')
plt.title('Sine and Cosine Waves')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right', fontsize=12, shadow=True, title='Legend')
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# 스타일 리스트
# styles = ['bmh', 'classic', 'dark_background', 'fivethirtyeight', 'ggplot',
#           'grayscale', 'Solarize_Light2', 'tableau-colorblind10']
#
# # 스타일 적용 예제
# for style in styles:
#     plt.style.use(style)
#     x = np.arange(0, 10, 0.1)
#     y1 = np.sin(x)
#     y2 = np.cos(x)
#
#     plt.plot(x, y1, label='Sine')
#     plt.plot(x, y2, label='Cosine')
#     plt.title('Sine and Cosine Waves')
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.legend()
#     plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 2x2 서브플롯 예제
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 2x2 서브플롯 생성

plt.subplot(2, 2, 1) # 몇 행 몇열 몇번째 칸에 넣을지 인덱스
plt.plot(x,y1)
plt.title('Sine')

plt.subplot(2, 2, 3)
plt.plot(x,y1)
plt.title('Sine')

plt.subplot(1, 2, 2)
plt.plot(x,y1)
plt.title('Sine')

plt.show()


# 첫 번째 서브플롯

'''
fig, axs = plt.subplots(2, 2, figsize=(4, 4))
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine')

# 두 번째 서브플롯
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine')

# 세 번째 서브플롯
axs[1, 0].plot(x, y1 + y2)
axs[1, 0].set_title('Sine + Cosine')

# 네 번째 서브플롯
axs[1, 1].plot(x, y1 - y2)
axs[1, 1].set_title('Sine - Cosine')

plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

labels = ['apple', 'banana', 'orange', 'grape', 'kiwi']
values = [20, 10, 15, 25, 30]

plt.bar(labels, values)
plt.show()
