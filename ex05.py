# for 문을 이용하여 팩토리얼을 계산하는 프로그램을 작성해보자.

fact=1.0
n =int(input("팩토리얼 값을 구할 정수를 입력 : "))

for i in range(1, n+1):
    fact*=i

print(n,"!은", fact ,"입니다.")