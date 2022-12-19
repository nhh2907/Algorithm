# https://school.programmers.co.kr/learn/courses/30/lessons/120923
def solution(num, total):
    lis = [i for i in range(-total-num, num+total+1)]
    
    i = 0
    while sum(lis[i:i+num]) != total:
        i += 1
        
    return lis[i:i+num]

# Best
def solution(num, total):
	### sum of offsets = num(num-1) / 2
	base = total - num * (num-1) / 2
	start = int(base // num)
	answer = list(range(start, start+num))
   	return answer
