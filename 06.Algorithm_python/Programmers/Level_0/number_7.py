# https://school.programmers.co.kr/learn/courses/30/lessons/120912
def solution(array):
    i = ''
    for num in array:
        i = i+str(num)
    
    count = 0
    for digit in i:
        if digit == '7':
            count += 1
    return count

# best
def solution(array):
    return str(array).count('7')

# best
def solution(array):
    return ''.join(map(str, array)).count('7')