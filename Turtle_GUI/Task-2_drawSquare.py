from turtle import Turtle, Screen

laya = Turtle()
laya.shape("turtle")

# TODO: To draw a square
for i in range(0,4):
    laya.forward(100)
    laya.right(90)
    
# laya.forward(100)
# laya.right(90)
# laya.forward(100)
# laya.right(90)
# laya.forward(100)
# laya.right(90)
# laya.forward(100)


scr = Screen()
scr.exitonclick()