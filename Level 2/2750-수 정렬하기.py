# N개의 수가 주어졌을때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 첫째 줄부터 n개의 줄에 오름차순으로 정렬한 결과를 한줄에 하나씩 출력한다.

N = int(input())
M = []
for i in range(N):
    M.append(int(input()))

M = sorted(M)
for i in range(len(M)):
    print(M[i])