import turtle



james = turtle.Turtle()
gwynn = turtle.Turtle()
poq = turtle.Turtle()




def weather_info():
    james.hideturtle()
    james.penup()
    gwynn.hideturtle()
    gwynn.penup()
    poq.hideturtle()
    poq.penup()

#Write time until next slack tide



    james.goto(-420, -250)
    gwynn.goto(-20,-250)
    poq.goto(380,-250)

    james.write("Time until slack:  ", align ="right", font=("Arial", 16, "normal"))
    gwynn.write("Time until slack:  ", align ="right", font=("Arial", 16, "normal"))
    poq.write("Time until slack:  ", align ="right", font=("Arial", 16, "normal"))


#Write precipitation chance key


    james.goto(-420, -280)
    gwynn.goto(-20,-280)
    poq.goto(380,-280)

    james.write("Current Weather:  ", align ="right", font=("Arial", 16, "normal"))
    gwynn.write("Current Weather:  ", align ="right", font=("Arial", 16, "normal"))
    poq.write("Current Weather:  ", align ="right", font=("Arial", 16, "normal"))


    #Write wind speed key

    james.goto(-420, -310)
    gwynn.goto(-20,-310)
    poq.goto(380,-310)

    james.write("Current Wind Speed:  ", align ="right", font=("Arial", 16, "normal"))
    gwynn.write("Current Wind Speed:  ", align ="right", font=("Arial", 16, "normal"))
    poq.write("Current Wind Speed:  ", align ="right", font=("Arial", 16, "normal"))


james_t = turtle.Turtle()
gwynn_t = turtle.Turtle()
poq_t = turtle.Turtle()
james_t.hideturtle()
james_t.penup()
gwynn_t.hideturtle()
gwynn_t.penup()
poq_t.hideturtle()
poq_t.penup()
james_t.goto(-350, -250)
gwynn_t.goto(50, -250)
poq_t.goto(450, -250)

def slack_update(slack1, slack2, slack3):

    james_t.clear()
    gwynn_t.clear()
    poq_t.clear()

    james_t.write(str(slack1) , align="center", font=("Arial", 16, "normal"))
    gwynn_t.write(str(slack2), align="center", font=("Arial", 16, "normal"))
    poq_t.write(str(slack3), align="center", font=("Arial", 16, "normal"))


james_w = turtle.Turtle()
pr_w = turtle.Turtle()
poq_w = turtle.Turtle()
james_w.hideturtle()
james_w.penup()
pr_w.hideturtle()
pr_w.penup()
poq_w.hideturtle()
poq_w.penup()
james_w.goto(-350, -280)
pr_w.goto(50, -280)
poq_w.goto(450, -280)


def weather_update(weath1, weath2, weath3):
    james_w.clear()
    pr_w.clear()
    poq_w.clear()
    james_w.write(weath1 , align="center", font=("Arial", 16, "normal"))
    pr_w.write(weath2 , align="center", font=("Arial", 16, "normal"))
    poq_w.write(weath3, align="center", font=("Arial", 16, "normal"))



james_wind = turtle.Turtle()
pr_wind = turtle.Turtle()
poq_wind = turtle.Turtle()
james_wind.hideturtle()
james_wind.penup()
pr_wind.hideturtle()
pr_wind.penup()
poq_wind.hideturtle()
poq_wind.penup()
james_wind.goto(-360, -310)
pr_wind.goto(40, -310)
poq_wind.goto(440, -310)


def wind_update(wind1, wind2, wind3):
    james_wind.clear()
    pr_wind.clear()
    poq_wind.clear()
    james_wind.write(str(wind1) + " mph", align="right", font=("Arial", 16, "normal"))
    pr_wind.write(str(wind2) + " mph", align="right", font=("Arial", 16, "normal"))
    poq_wind.write(str(wind3) + " mph", align="right", font=("Arial", 16, "normal"))

