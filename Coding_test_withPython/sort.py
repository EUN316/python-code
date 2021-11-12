# 이것이 취업을 위한 코딩테스트다 with 파이썬
# CHAPTER 06. Sort

# Example 6-1. 선택 정렬
def selection_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_idx = i # 최소값을 갖는 index 초기화
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]: # j가 더 작으면
                min_idx = j # 업데이트
        # 가장 작은 값을 지나오지 않은 맨 앞과 교체
        array[i], array[min_idx] = array[min_idx], array[i] 
    
    return array


# Example 6-3. 삽입 정렬
def insertion_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(array)): # 두번째부터 시작
        for j in range(i, 0, -1): # i번째부터 감소
            if array[j] < array[j-1]: # 앞에 있는 숫자보다 더 작으면
                array[j], array[j-1]  = array[j-1], array[j] # 교체
            else: # 앞에 있는 숫자보다 더 크면, 즉 더 작은 데이터를 만나면
                break
    
    return array


# Example 6-4. 퀵 정렬
def quick_sort(array, start, end):
    if start >= end: # 남은 리스트 길이가 1이면
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]: # pivot보다 클 때까지
            left += 1
        while right > start and array[right] >= array[pivot]: # pivot보다 작을 때까지
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else: # 교차되면
            array[right], array[pivot] = array[pivot], array[right] # pivot과 right를 교체
        
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


# Example 6-5. 퀵 정렬 python 버전
def quick_sort_python(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 첫번째가 pivot
    arr = array[1:] # pivot을 제외한 리스트

    left_side = [i for i in arr if i <= pivot]
    right_side = [i for i in arr if i > pivot]

    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)


# Example 6-6. 계수 정렬
def counting_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

    count = [0 for _ in range(max(array)+1)] # max값만큼 0으로 채운 리스트 생성

    for i in array:
        count[i] += 1 # 1씩 증가

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


# Example 6-7,8,9. 정렬 라이브러리
def setting(data):
    return data[1]

def sort_library():
    array = [7, 5, 9, 0, 4, 1, 6, 2, 4, 8]

    result = sorted(array)
    print(result)

    array.sort()
    print(array)

    array = [('바나나',2), ('사과',5), ('당근',3)]
    result = sorted(array, key=setting)
    print(result)


# Example 6-10. 위에서 아래로
def exam_6_10():
    n = int(input())
    array = [int(input()) for _ in range(n)] # n개만큼 입력 받기

    array = sorted(array, reverse=True)

    for i in array:
        print(i, end=' ')


# Example 6-11. 성적 낮은 순
def exam_6_11():
    n = int(input())
    
    array = [] 
    for _ in range(n):
        name, score = input().split(' ')
        array.append([name, score])

    array = sorted(array, key = lambda x:x[1], reverse=True) # 성적 내림차순

    for i in array:
        print(i[0], end=' ')

# Example 6-12. 두 배열 원소 교체
def exam_6_12():
    n, k = map(int, input().split())
    arr1 = list(map(int, input().split()))[:n]
    arr2 = list(map(int, input().split()))[:n]

    arr1.sort() # 오름차순
    arr2.sort(reverse=True) # 내림차순

    for i in range(k):
        if arr1[i] < arr2[i]:
            arr1[i], arr2[i] = arr2[i], arr1[i] # 교체
        else:
            break

    return sum(arr1) # 합 반환



if __name__=="__main__":
    print('Sort')
    # print('selection sort: ', selection_sort())
    # print('insertion sort: ', insertion_sort())
    # array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    # quick_sort(array, 0, len(array))
    # print('quick sort: ', array)
    # print('quick sort python: ', quick_sort_python(array))
    # print('counting sort: ', counting_sort())
    # print('sort library: ', sort_library())
    # exam_6_10()
    # exam_6_11()
    print(exam_6_12())