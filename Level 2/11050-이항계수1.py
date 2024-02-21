# 우선 이항계수라는 개념부터 정리하는것이 좋겠다.
# 자연수 n 및 정수 k가 주어졌을때 이항계수는 다음과 같다.
# nCk 라고 생각하면 된다. ,(n/k)랑 똑같음
# nCk라면 n!/(k!(n-k)!)
# 4C2라면, 4*3*2*1/(2*1(2*1))
# 4C2, 4*3/2*1
# 5C2 = 5*4/2*1
# 파이썬 math 라이브러리에 있는 팩토리얼 함수를 사용해서 만들었고,
# for 반복문이나 재귀함수를 사용해서 팩토리얼 함수를 만들어보는것도 도움이 되겠다.

import math

a,b = map(int,input().split())
result=0

if b<0 :
    print("0")
elif b>a :
    print("0")
else :
    result=(math.factorial(a))/((math.factorial(b))*(math.factorial(a-b)))
    print(int(result))