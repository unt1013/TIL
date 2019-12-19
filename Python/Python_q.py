str = input('문자를 입력하세요: ')
# 아래에 코드를 작성해 주세요.

print(str[0], str[-1])

numbers = int(input('숫자를 입력하세요: '))

for i in range(numbers + 1) :
    print(i)

if numbers % 2 :
    print("홀수")
else :
    print("짝수")