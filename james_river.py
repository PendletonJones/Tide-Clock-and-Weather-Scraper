
#This module determines current tide height for animation and timedelta purposes at the James River Fall Line



import turtle
import datetime
import time



offset = 65    #plus or minus number of 5 minute periods off from standard clock
j_t = turtle.Turtle()

def james_align(time_from_closest_low):
    j_t.color("cyan")
    j_t.showturtle()
    j_t.penup()
    total_time_offset = offset + time_from_closest_low
    if -74 <= total_time_offset <= 74:
        y = (-130 + abs(total_time_offset) * (280/74))
        j_t.goto(-400, y)
    elif total_time_offset > 74 or total_time_offset < -74:
        y = (150 - abs(total_time_offset-74) * (280 / 74))
        j_t.goto(-400, y)
    else:
        print("James Align Error")



def james_animation(counter, time_from_closest_low):
    '''
    One tide cycle is 12 hours, 25 minutes or 149, 5 minute periods.
    Taking away one 5 minute period to help account for process delays,
    that leaves 148 5 minute periods (counter values) for the animation
    '''
    j= counter + (offset + time_from_closest_low)
    if 0 <= j < 74:
        j_t.seth(90)
        j_t.fd(280 / 74)

    elif 74 <= j < 148:
        j_t.seth(270)
        j_t.fd(280/ 74)

    elif 148 <= j < 222:
        j_t.seth(90)
        j_t.fd(280 / 74)

    elif j >=222:
        j_t.seth(270)
        j_t.fd(280 / 74)

    elif j < 0:
        j_t.seth(270)
        j_t.fd(280 / 74)

    else:
        print('James animation error')


def james_slack_calc(counter, time_from_closest_low):
    j = counter + (offset + time_from_closest_low)
    if 0 <= j < 74:
        t = (73 - j) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif 74 <= j < 148:
        t = (147 - j) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif 148 <= j > 222:
        t = (221 - j) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif j >= 222:
        t = (295 - j) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif j < 0:
        t = (- j) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    else:
        print("James slack calculation error")
        
