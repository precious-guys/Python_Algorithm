# A, B = map(int, input().split())
# C = int(input())
# a = A * 60 + B + C
# print(f'{a//60} {a % 60}') if a//60 < 23 else print(f'{(a - 24*60)//60} {a % 60}')


A, B = map(int, input().split())
C = int(input())

A += C // 60
B += C % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24
print(f"{A} {B}")