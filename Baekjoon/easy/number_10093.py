# https://www.acmicpc.net/problem/10093
M, N = sorted(map(int, input().split()))
def count_int(M, N):
    if M == N: return print(0)
    print(N-M-1)
    print(' '.join(map(str, range(M+1, N))))

count_int(M, N)