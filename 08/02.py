# 실기2 진약수의 합

a = int(input())
k = 0

for i in range(a) :
    if (i+1)==a :
        break
    elif a%(i+1)==0 :
        k+=i+1

if k < a :
    print("부족수")
elif k == a :
    print("완전수")
else :
    print("과잉수")