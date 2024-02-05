# 백준 1978번 소수찾기
n = int(input())
numbers = map(int, input().split())

prime = 0
for num in numbers:
    error = 0
    if num > 1 : #숫자가 1이상 일때
        for i in range(2, num): #소수는 1과 자기자신을 제외한 수 외로 나누어지지 않는 수이기 때문에 2부터 자기자신-1로 나눈다.
            if num % i == 0: # 2~n-1로 나누었을때 나머지가 0이면
                error += 1 # 에러에 1을 더한다.
        if error == 0: # 만약에 에러가 0이라면(나누었을때 나머지가 0이 아님=소수)
            prime += 1 # 소수의 개수에 1을 추가, 소수의 개수를 구할 수 있다.

print(prime) #위의 코드들로 인해 소수의 개수를 출력할 수 있다. 