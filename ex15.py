# 사용자로부터 상품금액을 입력받아서 상품의 총 가격을 계산하는 프로그램 만들기
# 사용자가 몇개의 상품을 살 지 모르니깐 무한루프를 이용하고, 사용자가 "끝"이라고 입력 하면 루프를 탈출하게 조건을 준다.

from operator import eq
total=0
price=""
while True:
    price=input("상품금액을 입력하세요(끝을 입력하면 종료됨) : " )
    # "끝"이라는 입력문구가 있는지 확인하는 코드, 무한루프를 탈출하는 코드
    if eq(price, "끝"):
        print("상품의 총 가격 : "+ str(total)+"원")
        break
    total+=int(price)
        