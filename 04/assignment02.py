xl=[]
while True:
    temp=int(input())
    if temp<0:
        break
    xl.append(temp)
print("최고 매출액:",max(xl))
print("최저 매출액:",min(xl))