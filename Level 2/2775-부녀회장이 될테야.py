# a층의 b호에 살려면 자신의 아래(a-1)층 의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야한다.
# ex) 7층의 b호에 살려면 자신의 아래 6층의 1호부터 b호까지의 사람들의 수의 합만큼 데리고 살아야한다.
# k층에 n호에는 몇명이 살고 있는지 출력.
# 아파트에는 0층부터 있고 각 층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

def calculate_residents(k, n):
    apartment = [[i for i in range(1, n+1)]]
    for i in range(1, k+1):
        residents = [sum(apartment[i-1][:j+1]) for j in range(n)]
        apartment.append(residents)
        return apartment[k][n-1]


T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    print(calculate_residents(k, n))