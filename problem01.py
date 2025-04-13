# 동아리원 필터링 프로그램

mem = list()
out = list()
mem=list(input().split('\n')) # 타입 변환 후 비교연산자 가능.

for i in range(len(mem)) :
    if mem[i] == 'END' :
        break
    elif mem[i]>=2300000 :
        out=mem[i]

print(out)