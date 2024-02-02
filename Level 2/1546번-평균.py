# 최댓값 추출 -> 원점수/최댓값*100 하여 새로운 평균

subject = int(input())
score = list(map(int, input().split()))
M = max(score)

for i in range(subject):
    score[i] = score[i]/M*100

print(sum(score)/subject)