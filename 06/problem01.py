# 동아리원 필터링 프로그램

mem = list()

while True:
    mem_=input()
    if mem_ == 'END' :
        break
    mem.append(mem_)

name=list()
for mem_ in mem :
    year = int(mem_[:2])

    if year >= 23:
        id, nam = mem_.split()
        mem.append(nam)

print(name)