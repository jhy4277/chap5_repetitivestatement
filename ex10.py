# 터틀그래픽을 활용하여 별모양을 그려본느 프로그램을 작성하시오. for 문이용

import turtle

t= turtle.Pen()

for i in range(5):
    t.forward(50)
    t.right(144)

turtle.exitonclick()