# https://school.programmers.co.kr/learn/courses/30/lessons/120863
def solution(polynomial):
    v = 0
    c = 0
    for num in polynomial.split(' + '):
        if 'x' in num:
            if 'x' == num:
                num = num.replace('x', '1')
            num = num.replace('x', '')
            v += int(num)
        else:
            c += int(num)
            
    if v != 0 and c != 0:
        if v == 1:
            answer = f'x + {c}'
        else:
            answer = f'{v}x + {c}'
    elif v == 0:
        answer = f'{c}'
    elif c == 0:
        if v != 1:
            answer = f'{v}x'
        else:
            answer = f'x'
    return answer


# best
def solution(polynomial):
    v = 0
    c = 0
    for num in polynomial.split(' + '):
        if num.isdigit():
            c += int(num)
        else:
            v = v+1 if num == 'x' else v+int(num[:-1])
    if v == 0:
        answer = str(c)
    elif v == 1:
        answer = f'x + {c}' if c!=0 else 'x'
    else:
        answer = f'{v}x + {c}' if c!=0 else f'{v}x'
    return answer