a,b = map(int,input().split())
c = 0
result = 0

# def fact(n):
#     result = 1
#     for i in range(1,n+1):
#         result *= i
#     return result

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

if b<0 :
    print("0")
elif b>a :
    print("0")
else :
    result = fact(a)//(fact(b) * fact(a-b))
    print(int(result))