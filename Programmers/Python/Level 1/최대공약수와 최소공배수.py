"""
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

두 수는 1이상 1000000이하의 자연수입니다.
"""
# Solution 1. 유클리드 호제법
def solution(n, m):
    answer = []
    # x가 y보다 크도록 값 삽입
    if n > m: 
        x, y = n, m
    else:
        x, y = m, n
    # 최대공약수: 유클리드 호제법
    while y:
        x, y = y, x%y
    answer.append(x)
    # 최소공배수: 최대공약수를 활용
    answer.append((n*m)//x)
    
    return answer

# Solution 2. gcd()
import math
def solution(n, m):
    # math.gcd 함수 사용하여 최대공약수 계산
    answer = [math.gcd(n, m), (n * m // math.gcd(n, m))] # 최대공약수, 최소공배수
    return answer