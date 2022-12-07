# https://www.acmicpc.net/problem/1225
A, B = input().split()
def anomaly_multiplication(m, n):
    A_list = list(map(int, list(A)))
    B_list = list(map(int, list(B)))

    return sum(A_list) * sum(B_list)

print(anomaly_multiplication(A, B))