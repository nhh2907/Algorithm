# https://school.programmers.co.kr/learn/courses/30/lessons/120853
def solution(s):
    answer = 0
    for num in s.split(): 
        if 'Z' != num:
            num = int(num)
            answer += num
        else:
            answer -= prev 
        prev = num

    return answer

# best
def solution(s):
	answer = 0
	for i in range(len(s := s.split())):
		answer += int(s[i]) if s[i] != 'Z' else -int(s[i-1])
	return answer

# best
def solution(s):
    arr = s.split(' ')
    result =[]
    for i in arr :
        if i=='Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)
