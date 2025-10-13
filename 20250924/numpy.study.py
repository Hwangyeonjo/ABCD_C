# -*- coding: utf-8 -*-
import numpy as np

a = [1, 2, 3, 4, 5]
b = np.array(a)

print("배열:", b)
print("타입:", type(b))
print("차원 수:", b.ndim)      # 배열의 차원 수 (1차원)
print("형태:", b.shape)        # 배열의 형태 (5,) - 5개 원소의 1차원
print("첫 번째 원소:", b[0])   # 배열의 첫 번째 원소 접근

# 2차원 배열 예시
c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)
print("2차원 배열의 차원 수:", c.ndim)
print("2차원 배열의 형태:", c.shape)  # (2, 3) - 2행 3열
print("2차원 배열 원소 접근 c[0,0]:", c[0, 0])  # 첫 번째 행, 첫 번째 열

#배열의 생성
c = np.zeros((2,2))
print(c)
d = np .zeros(5)
print(d)

e = np.ones((2,2))
print(e)

f = np.full((2,3),5)
print(f)