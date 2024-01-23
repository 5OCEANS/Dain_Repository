# 1259번: 팰린드롬수
# 뒤에서 읽어도 똑같은 radar 같은 수를 팰린드롬이라고 한다.
# 입력을 밥고 팰린드롬수면 yes, 아니면 no를 출력한다.

while True:
    n = input()

    if n == '0':
        break
    else:
        if n == n[::-1]: # 입력받은 수를 거꾸로 뒤집음
            print('yes')
        else:
            print('no')