# 두 개의 숫자를 입력받음
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 사칙연산 수행
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# 몫과 나머지 연산 수행
quotient = num1 // num2
remainder = num1 % num2

# 결과 출력
print("덧셈 결과:", addition)
print("뺄셈 결과:", subtraction)
print("곱셈 결과:", multiplication)
print("나눗셈 결과:", division)
print("몫:", quotient)
print("나머지:", remainder)

# 비교 연산 수행
greater_than = num1 > num2
less_than = num1 < num2
equal_to = num1 == num2
not_equal_to = num1 != num2

print("첫 번째 숫자가 두 번째 숫자보다 큰가?", greater_than)
print("첫 번째 숫자가 두 번째 숫자보다 작은가?", less_than)
print("두 숫자가 같은가?", equal_to)
print("두 숫자가 다른가?", not_equal_to)

# 대입 연산자의 종류와 활용
num1 += num2
print("+= 연산 후 결과:", num1)

num1 -= num2
print("-= 연산 후 결과:", num1)

num1 *= num2
print("*= 연산 후 결과:", num1)

num1 /= num2
print("/= 연산 후 결과:", num1)

num1 //= num2
print("//= 연산 후 결과:", num1)

num1 %= num2
print("%= 연산 후 결과:", num1)


# 논리 연산 수행
logical_and = num1 > 0 and num2 > 0
logical_or = num1 > 0 or num2 > 0
logical_not = not (num1 > 0)

# 결과 출력
print("첫 번째 숫자와 두 번째 숫자 모두 양수인가?", logical_and)
print("첫 번째 숫자 또는 두 번째 숫자 중 어느 하나가 양수인가?", logical_or)
print("첫 번째 숫자가 양수가 아닌가?", logical_not)

