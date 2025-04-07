# 풀이 1: 무한 반복 활용
min_sales = 1_000_000_000  # 최초의 입력을 반드시 최솟값으로 간주할할 수 있는 초깃값 10억을 최소 매출액으로 지정
max_sales = 0  # 최초의 입력을 반드시 최댓값으로 간주할 수 있는 초기값 0을 최대 매출액으로 지정

while True:
    n = int(input())
    if n < 0:
        break

    if n < min_sales:
        min_sales = n
    if n > max_sales:
        max_sales = n

print('최고 매출액:', max_sales)
print('최저 매출액:', min_sales)

# # Visual Studio Code와 Jupyter Notebook 에서 [Ctrl+/] 단축키를 활용하시면 여러 줄의 주석을 걸고 풀 수 있습니다. 아래 코드를 드래그한 뒤, 단축키를 눌러보세요.
# # macOS에서도 [⌘/] 단축키로 가능합니다.

# # 풀이 2: while의 조건식으로 반복 여부를 결정.
# min_sales = 1_000_000_000  # 최초의 입력을 반드시 최솟값으로 간주할할 수 있는 초깃값 10을 최소 매출액으로 지정
# max_sales = 0  # 최초의 입력을 반드시 최댓값으로 간주할 수 있는 초기값 0을 최대 매출액으로 지정
#
# n = int(input())
# while n >= 0: # n이 0이거나 양수인 동안 반복한다.
#     if n < min_sales:
#         min_sales = n
#     if n > max_sales:
#         max_sales = n
#     n = int(input())
#
# print('최고 매출액:', max_sales)
# print('최저 매출액:', min_sales)
#
#
# # 풀이 3: **아직 배우지 않은** 리스트 활용
#
# list_sales = list()
# while True:
#     sale = int(input())
#     if sale < 0:
#         break
#     else:
#         list_sales.append(sale)
#
# print('최고 매출액:', max(list_sales)) # 리스트에 담긴 값중 최댓값을 max() 내장 함수로 얻는다.
# print('최저 매출액:', min(list_sales)) # 리스트에 담긴 값중 최솟값을 min() 내장 함수로 얻는다.
