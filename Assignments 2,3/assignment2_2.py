num = int(input('Enter a digit between 0 and 999: ')) # 입출력 요구사항에 따라 사용자에게 가이드 문자열을 제시해야 함

sum_digits = num // 100
sum_digits += (num // 10) % 10
sum_digits += num % 10

print('The sum of digits is', sum_digits)

# record assignment2_2.svg
# python assignment2_2.py
# 999

# python assignment2_2.py
# 17

# python assignment2_2.py
# 123
