# 사용자로부터 출력하고 싶은 구구단을 출력하는 프로그램을 만들기

num= int(input("출력하고 싶은 단을 출력하세요  :"))
for i in range(1, 10):
    if (num<2) or (num>9):
        print("단을 잘못입력하셨습니다.")
        break
    print(num, "*",i,"=",num*i)
