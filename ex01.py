# 반복문(iteration)에 대한 실습

for x in [0,1,2,3,4]:
    print("안녕하세요")
# x를 루프변수라 칭하며 in 다음에 오는 것을 시퀀스라고 칭한다.
# 시퀀스에 올 수 있는 것은 리스트, 문자열이 가능하다.

print("--------------")

# range(x)함수를 사용하면 정수 리스트를 사용하는 것보다 훨씬 효율적인 코드이며, 가독성도 좋다.
# range()함수는 리스트 타입으로 반환해준다.
# range(x) : 0부터 마지막값까지 (x-1)까지 정수 리스트 타입으로 출력해준다.
for x in range(5):
    print("안녕하세요")
# range() 함수의 타입은 range 객체타입이다.
print(type(range(5)))

# 문자열 리스트를 시퀀스로 가질 때의 for문
s=["정혜원", "박성현","뷔","진"]
for name in s:
    print("반갑습니다 "+name+" 님")

# 줄바꿈을 하지 않게 하는 end 인자값을 확인해보기
for x in [0,1,2,3,4]:
    print(x,end="\t ")