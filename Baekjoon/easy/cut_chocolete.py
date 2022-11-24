# https://www.acmicpc.net/problem/2163

M, N = map(int, input().split())
def cut_chocolete(M, N):
    return (M * N) - 1

print(cut_chocolete(M, N))