# range() 함수 실습하기

# 1. range(x) 매개변수 1개자리 함수를 이용
hap=0
for x in range(10):
    hap=hap+x
print("1. 0부터 9까지 누계합: ", hap)

# 2. range(start, stop) 매개변수 2개짜리
# 누적을 하는데 stop 값은 포함하지 않는다.
hap=0
for x in range(0,10):
    hap=hap+x
print("2. 0부터 9까지 누계합: ", hap)

# 2. range([start,] stop, [step]) 매개변수 23개짜리
# []로 감싸져 있는 것들은 생략 가능
# 누적을 하는데 stop 값은 포함하지 않는다. 누적을 시킬때 step만큼 건너뛰어 리스트를 생성한다.

hap=0
for x in range(0,10,1):
    hap=hap+x
print("3. 0부터 9까지 누계합: ", hap)

# 문자열 실습
# 문자열도 시퀀스의 대상에 포함된다. for 문을 통해 문자를 추출하여 출력할 수 있다.

s="Jeong Hea won"
for ch in s:
    print(ch, end=" ")