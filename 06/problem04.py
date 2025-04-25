# 코딩 대회 생존자 판별

score=list(map(int,input().split()))
score.remove(min(score))
print(score)
# 출력값 none으로 나오는거 수정 필요