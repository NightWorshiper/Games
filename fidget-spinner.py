from turtle import *
state = {'turn': 0}
def spinner():
    clear()
    angle = state['turn']/15
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()
def animate():
    if state['turn']>0:
        state['turn']-=1
    spinner()
    ontimer(animate, 20)
def flick():
    state['turn']+=10

setup(420, 420, 360, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()


# Coded with 💙 by Mr. Unity Buddy
