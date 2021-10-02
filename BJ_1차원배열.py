#1

import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))

print(min(num), max(num))


#2

import sys

input = sys.stdin.readline

n = []

for i in range(9):
    n.append(int(input()))

print(max(n))

print(n.index(max(n))+1)


#3

import sys

input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))

#4


import sys

input = sys.stdin.readline

num = []

for i in range(10):
    n = int(input())
    num.append(n % 42)

num = set(num)

print(len(num))


#5

import sys

input = sys.stdin.readline

n = int(input())

test_list = list(map(int, input().split())) # 각기 다른 문자나 숫자를 스플릿 해서 담는 방법
max_score = max(test_list) # 최대수를 구하는 방법

new_list = []

for i in test_list:
    new_list.append(i / max_score * 100)

test_avg = sum(new_list) / n

print(test_avg)


#6

import sys

input = sys.stdin.readline

n = int(input())



for i in range(n):
    test = str(input())
    score = 0
    c = 1
    for j in test:
        if j == 'O':
            score += c
            c += 1
        else:
            c = 1
    print(score)


#7

import sys

input = sys.stdin.readline

test_num = int(input())

for i in range(test_num):
    student_num = list(map(int, input().split()))
    avg = (sum(student_num[1:]) / student_num[0])
    cnt = 0
    for score in student_num[1:]:
        if score > avg:
            cnt += 1  #평균 이상인 학생 수
    rate = cnt / student_num[0] * 100
    print(f'{rate:.3f}%')
