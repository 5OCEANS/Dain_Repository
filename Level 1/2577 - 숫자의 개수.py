# 2577번 숫자의 개수
# 계산한 결과에 0부터 9까지 각각의 숫자가 몇번 쓰였는지 구하는 프로그램

a = int(input())
b = int(input())
c = int(input())
result = list(str(a*b*c)) #a*b*c를 문자열(str)로 변환한 후 list[]로 묶는다.
                        # 그럼 각각의 index로 저장된다.

for i in range(10): # 0~9
    print(result.count(str(i))) #count를 사용해서 개수를 센다.