x1, y1 = map(float, input('Enter x1 and y1: ').split()) # 입출력 요구사항에 따라 사용자에게 가이드 문자열을 제시해야 함
x2, y2 = map(float, input('Enter x2 and y2: ').split()) # 입출력 요구사항에 따라 사용자에게 가이드 문자열을 제시해야 함

d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 # 이 부분에는 별도의 해석이 없습니다.
print('The distance of the two points is', d)
