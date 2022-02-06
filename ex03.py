# 1부터 사용자가 입력한 수 num 까지 더해서 합계를 구하는 프로그램 for 문을 작성하시오.
hap=0
num=int(input("어디까지 합계를 구하겠습니까? : "))

for i in range(1,num+1):
    hap+=i

print("1부터 ", num, "까지의 정수의 합계 = ", hap)