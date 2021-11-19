"""
완전탐색

한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
"""
from itertools import permutations

def prime_number(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**(1/2))+1): # 2~sqrt(n)
        if n % i == 0: # 소수가 아니면
            return False
    return True


def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1): # 1 ~ numbers 개수
        for comb in list(permutations(numbers, i)): # i개 원소로 이루어진 순열
            comb = int(''.join(comb)) # int로 변환
            if comb not in answer: # '0'으로 시작하지 않는 경우만
                if prime_number(comb) == True: # 소수이면
                    answer.append(comb)
    
    return len(answer)