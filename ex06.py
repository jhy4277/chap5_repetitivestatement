# 피보나치 수열을 구하는 프로그램을 만들기
# 앞의 2개의 수를 더해서 다음 수를 결정 짓는 수열

n1=1
n2=1
n3=1

fi=int(input("피보나치수열을 만들 정수를 입력하세요 : "))

for i in range(1, fi):
    if i <3 :
        n3 = 1
    else:
        n3 = n1+n2
        n1=n2
        n2=n3
    if n3<fi:
        print(n3, end= " ")

