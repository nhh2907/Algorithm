# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    temp = arr[0]
    answer = [temp]
    for i in arr:
        if i != temp:
            temp = i
            answer.append(i)
    return answer

def solution(arr):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a