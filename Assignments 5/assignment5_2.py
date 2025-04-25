def ReLU(x):  # ReLU 함수 구현
    if x <= 0.0:
        return 0.0
    else:
        return x


x = float(input(f'x='))  # 실수 입력 받기
print(f'ReLU({x})={ReLU(x)}')  # ReLU 함수 결과 출력
