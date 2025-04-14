# 가사 속 알파벳 수 세기

lyrics=list(input("lyrics="))
key=input("alphabet")
time=0

for i in lyrics :
    if i==key :
        time+=1

print(time)