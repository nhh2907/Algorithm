# https://school.programmers.co.kr/learn/courses/30/lessons/120880
def solution(numlist, n):
    list_temp = [num-n for num in numlist]
    list_temp = sorted(list_temp, key=lambda x : (abs(x), x*(-1))) # https://stackoverflow.com/questions/5212870/sorting-a-python-list-by-two-fields

    answer = [n+num for num in list_temp]

    return answer


