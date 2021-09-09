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


# Example 6-2. 삽입 정렬
def insertion_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(1, len(array)): # 두번째부터 시작
        for j in range(i, 0, -1): # i번째부터 감소
            if array[j] < array[j-1]: # 앞에 있는 숫자보다 더 작으면
                array[j], array[j-1]  = array[j-1], array[j] # 교체
            else: # 앞에 있는 숫자보다 더 크면, 즉 더 작은 데이터를 만나면
                break
    
    return array



if __name__=="__main__":
    print('Sort')
    print('selection sort: ', selection_sort())
    print('selection sort: ', insertion_sort())