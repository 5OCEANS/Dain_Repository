# 최대공약수, 최소공배수 구하는방법을 다시 공부하기
# 최대 공약수는 나눌 수 있는만큼 나눠서 나눈 몫을 곱하면된다.
# 최대 공배수는 나눌 수 있는만큼 나눠서 나눈 몫과 나머지를 곱하면 된다.

def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a

def lcd(a,b):
    return a*b // gcd(a,b)

a, b = map(int, input().split())

gcd_result = gcd(a,b)
lcd_result = lcd(a,b)

print(gcd_result)
print(lcd_result)
