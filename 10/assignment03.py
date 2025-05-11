# 데이터 분석기

path=input()
num=[]

fp=open(f"{path}","rt")

lines=fp.read().splitlines()
for line in lines :
    num.append(int(line))

num.sort()

if len(num)%2==0 :
    avg=sum(num)/len(num)
    median=(num[len(num)//2]+num[len(num)//2-1])/2
else :
    avg=sum(num)/len(num)
    median=num[len(num)//2]


print(f'평균: {avg:.1f} / 중앙값: {median:.1f}')

fp.close