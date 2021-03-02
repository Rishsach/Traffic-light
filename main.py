import turtle           # Tess becomes a traffic light.
 
 
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
alexis = turtle.Turtle()
 
 
def draw_housing2():
    """ Draw a nice housing to hold the traffic lights """
    alexis.pensize(3)
    alexis.color("black", "darkgrey")
    alexis.penup()
    alexis.backward(180)
    alexis.pendown()
    alexis.begin_fill()
    alexis.forward(80)
    alexis.left(90)
    alexis.forward(275)
    alexis.circle(40, 180)
    alexis.forward(275)
    alexis.left(90)
    alexis.end_fill()
 
def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()
 
 
 
draw_housing()
draw_housing2()
 
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("green")
alexis.penup()
alexis.forward(40)
alexis.left(90)
alexis.forward(50)
alexis.shape("circle")
alexis.shapesize(3)
alexis.fillcolor("gray")
bob = turtle.Turtle()
bob.penup()
bob.goto(alexis.position()[0], (alexis.position()[1] + 75))
bob.shape('circle')
bob.shapesize(3)
bob.fillcolor("gray")
chris = turtle.Turtle()
chris.penup()
chris.goto(bob.position()[0], (bob.position()[1] + 75))
chris.shape('circle')
chris.shapesize(3)
chris.fillcolor('gray')
jeff = turtle.Turtle()
jeff.penup()
jeff.goto(chris.position()[0], (chris.position()[1] + 75))
jeff.shape('circle')
jeff.shapesize(3)
jeff.fillcolor('gray')
 
# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.
 
# This variable holds the current state of the machine
state_num = 0
state_num_1 = 0
 
def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(70)
        tess.fillcolor("orange")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.forward(70)
        tess.fillcolor("red")
        state_num = 2
    else:                     # Transition from state 2 to state 0
        tess.back(140)
        tess.fillcolor("green")
        state_num = 0
    wn.ontimer(advance_state_machine, "5000")
 
def advance_state_machine2():
    global state_num_1
    if state_num_1 == 0:       # Transition from state 0 to state 1
        jeff.fillcolor('gray')
        alexis.fillcolor('green')
        state_num_1 = 1
    elif state_num_1 == 1:     # Transition from state 1 to state 2
        alexis.fillcolor('gray')
        bob.fillcolor('green')
        chris.fillcolor('orange')
        state_num_1 = 2
    elif state_num_1 == 2:
        bob.fillcolor('gray')
        chris.fillcolor('gray')
        jeff.fillcolor('red')
        state_num_1 = 0
    wn.ontimer(advance_state_machine2, "5000")
 
advance_state_machine()
advance_state_machine2()
 
wn.mainloop()