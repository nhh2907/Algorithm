# https://school.programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    list_nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, num in enumerate(list_nums):
        s = s.replace(num, str(i))
    return int(s)


# Best solution
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
