# instruction 
# 주어진 날짜로부터 2025년 봄학기 종강(2025년 6월 16일 월요일)까지 며칠 남았는지 D-day를 세는 프로그램을 구현하시오.
# 입력 : yyyy-mm-dd 형식의 날짜를 나타내는 문자열 | 출력 : 종강까지의 d-day
# ex | input : 2025-06-15 , output : D-1 
# ex | input : 2025-04-29 , output : D-48

import datetime as dt

a,b,c=map(int,input().split("-"))

dday = dt.datetime(2025,6,16)
gap = dday-dt.datetime(a,b,c)

print(f"D-{gap.days}")