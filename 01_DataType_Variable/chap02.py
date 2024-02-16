'''
자료형과 형변환
'''

height = 178.5
print(height, type(height))

# 실수 -> 정수
ki = int(height)
print(ki, type(ki))

# 정수 -> 실수
height = float(ki)
print(height, type(height))

# 문자열 -> 실수
height = "178.5"
height = float(height)
print(height, type(height))

# 실수 -> 문자열
height = str(height)
print(height, type(height))

# 문자열 -> 정수
ki = "178"
ki = int(ki)
print(ki, type(ki))

# 정수 -> 문자열
ki = str(ki)
print(ki, type(ki))


