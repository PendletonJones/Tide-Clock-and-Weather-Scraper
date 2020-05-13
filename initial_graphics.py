import turtle

def win_open():
    turtle_screen = turtle.Screen()
    turtle_screen.setup(width=1280, height=800)
    turtle_screen.bgcolor("orange")

def tide_scale():
    title = turtle.Turtle()
    james = turtle.Turtle()
    pr = turtle.Turtle()
    poq = turtle.Turtle()

    title.hideturtle()
    title.penup()
    james.hideturtle()
    james.penup()
    pr.hideturtle()
    pr.penup()
    poq.hideturtle()
    poq.penup()

    #Write title, location names, tide labels

    title.goto(0,300)
    james.goto(-400, 200)
    pr.goto(0,200)
    poq.goto(400,200)
    title.write("Virginia Coastal Tides & Weather", align ="center", font=("Arial", 20, "bold"))
    james.write("James River - Richmond", align ="center", font=("Arial", 16, "bold"))
    pr.write("Piankatank River - Gwynn's Island", align ="center", font=("Arial", 16, "bold"))
    poq.write("Poquoson River - Plum Island", align ="center", font=("Arial", 16, "bold"))
    james.goto(- 330, 150)
    james.write("High Tide", align="center", font=("Arial", 12, "bold"))
    pr.goto(70, 150)
    pr.write("High Tide", align="center", font=("Arial", 12, "bold"))
    poq.goto(470, 150)
    poq.write("High Tide", align="center", font=("Arial", 12, "bold"))
    james.goto(- 330, -130)
    james.write("Low Tide", align="center", font=("Arial", 12, "bold"))
    pr.goto(70, -130)
    pr.write("Low Tide", align="center", font=("Arial", 12, "bold"))
    poq.goto(470, -130)
    poq.write("Low Tide", align="center", font=("Arial", 12, "bold"))


    #Draw tide scale
    #Top y coor = 150, bottom y coor = -130

    james.goto(-400, 150)
    pr.goto(0, 150)
    poq.goto(400, 150)

    james.pencolor("white")
    james.pendown()
    pr.pencolor("white")
    pr.pendown()
    poq.pencolor("white")
    poq.pendown()

    james.fd(20)
    james.bk(40)
    james.fd(20)
    james.rt(90)
    james.fd(280)
    james.lt(90)
    james.fd(20)
    james.bk(40)

    pr.fd(20)
    pr.bk(40)
    pr.fd(20)
    pr.rt(90)
    pr.fd(280)
    pr.lt(90)
    pr.fd(20)
    pr.bk(40)

    poq.fd(20)
    poq.bk(40)
    poq.fd(20)
    poq.rt(90)
    poq.fd(280)
    poq.lt(90)
    poq.fd(20)
    poq.bk(40)
