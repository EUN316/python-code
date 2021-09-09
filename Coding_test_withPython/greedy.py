# 이것이 취업을 위한 코딩테스트다 with 파이썬
# CHAPTER 03. Greedy

# Example 3-1. 거스름돈
def exam_3_1():
    money = int(input("input Money: "))
    n = 0 # 동전 개수 초기화
    coins = [500, 100, 50, 10] # 동전 list
    
    for coin in coins: # 가장 큰 단위부터 아래로
        n += money // coin # 몫 = 그 동전을 거슬러줄 수 있는 개수
        money = money % coin
    
    return n


# Example 3-2. 큰 수의 법칙
def exam_3_2_1():
    # n, m, k 한번에 입력 후 나눠서 저장
    n, m, k = map(int, input("input N M K: ").split(' '))
    # n개만큼 자연수 입력 & 내림차순 정렬
    values = list(map(int, input("input values: ").split(' '))) 
    values.sort(reverse = True)

    first = values[0] # 가장 큰 수
    second = values[1] # 두번째로 큰 수

    sum_val = 0 # 합산 값 초기화

    while m!=0: # m번 만큼 다 돌면 break
        for i in range(k): # 한번에 k만큼 반복 가능
            sum_val += first
            m -= 1
            if m == 0:
                break
        
        sum_val += second # 두번째로 큰 값 한번만 더하기
        m -= 1 
        if m ==0:
            break

    return sum_val


# Example 3-2. 큰 수의 법칙 (더해지는 횟수를 구하는 방법)
def exam_3_2_2():
    # n, m, k 한번에 입력 후 나눠서 저장
    n, m, k = map(int, input("input N M K: ").split(' '))
    # n개만큼 자연수 입력 & 내림차순 정렬
    values = list(map(int, input("input values: ").split(' '))) 
    values.sort(reverse = True)

    first = values[0] # 가장 큰 수
    second = values[1] # 두번째로 큰 수

    # 가장 큰 수가 더해질 횟수를 계산
    count = (m//(k+1))*k + m%(k+1)

    sum_val = 0 # 합산 값 초기화
    sum_val += count * first
    sum_val += (m-count) * second

    return sum_val


# Example 3-3. 숫자 카드 게임
def exam_3_3():
    n, m = map(int, input("input N M: ").split(' '))
    maximum = 0 # 반환할 행마다 가장 작은 수 중 가장 큰 값
    for i in range(n): # 한 줄씩 입력받기
        cards = list(map(int, input("input cards: ").split(' ')))
        min_in_row = min(cards) # list 중 min값
        maximum = max([maximum, min_in_row]) # 현재 max값과 비교

    return maximum


# Example 3-4. 1이 될 때까지
def exam_3_5():
    n, k = map(int, input("input N K: ").split(' '))
    count = 0 # 수행 횟수

    while n > 1:
        while n%k != 0: # 나누어 떨어질 때까지
            n -= 1 # 1번
            count += 1
        
        n = n//k # 2번
        count += 1

    return count



if __name__ == "__main__":
    print('Greedy')
    print('exam_3_1: ', exam_3_1())
    print('exam_3_2: ', exam_3_2_1())
    print('exam_3_2: ', exam_3_2_2())
    print('exam_3_3: ', exam_3_3())
    print('exam_3_4: ', exam_3_5())
