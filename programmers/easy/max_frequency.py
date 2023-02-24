# https://school.programmers.co.kr/learn/courses/30/lessons/120812?language=python3
def solution(array):
    # 빈도수 딕셔너리 생성
    dic = {}
    for digit in array:
        if digit not in dic:
            dic[digit] = 1
        else:
            dic[digit] += 1

    # 내림차순 정렬 - 출력: 튜플 리스트
    sorted_dict = sorted(dic.items(), key=lambda x : x[1], reverse=True)
    
    # 0번 인덱스 제외한 나머지가 0번 인덱스 빈도수와 하나라도 같다면 -1, 그렇지 않으면 0번 인덱스 값 출력
    for tup in sorted_dict[1:]:
        if tup[1] == sorted_dict[0][1]:
            return -1
    return sorted_dict[0][0]

# best
def solution(array):
    while len(array) != 0:
        for idx, num in enumerate(set(array)):
            array.remove(num)
        if idx == 0: return num
    return -1
