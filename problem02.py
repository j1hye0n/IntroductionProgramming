# 청파마켓 반값 세일 계산기
price=list(map(int,input().split()))

for i in range(len(price)) :
    price[i]=int(price[i]*0.5)

print(price)