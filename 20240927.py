# ################ Quiz 1 #################
userinput1 = input("인사를 해주세요: ")

if userinput1 == "안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요.")

# ################ Quiz 2 #################
userinput2 = input("숫자를 입력하세요: ")

result = int(userinput2) + 100

if result >= 150:
    print(f"계산 결과: {result}")
else:
    print("값이 부족합니다.")

# ################ Quiz 3 #################
numbers = [100, 200, 300]

result1 = []

for price in numbers:
    tax_price = price * 1.1
    result1.append(int(tax_price))

print(result1)

# ################ Quiz 4 #################
numbers1 = [3, 100, 23, 33, 72, 94]

result2 = []

for num in numbers1:
    if num % 3 == 0:
        result2.append(num)

print(result2)

################ Quiz 5 #################
waiting_number = 1

while waiting_number <= 1000:
    print(f"대기번호: {waiting_number}")
    waiting_number = waiting_number + 1

################ Quiz 6 #################
number2 = 1
odd_sum = 0

while number2 <= 100:
    if number2 % 2 != 0:
        odd_sum = odd_sum + number2
    number2 = number2 + 1

print(f"1부터 100까지 존재하는 홀수의 합: {odd_sum}")