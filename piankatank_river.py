#This module determines current tide height for animation and timedelta purposes at the Piankatank River mouth

import turtle
import datetime
import time

#offset represents # of 5 minute periods the given tide is from the standard tide
offset = -11
pr_t = turtle.Turtle()

def piank_align(time_from_closest_low):
    pr_t.color("cyan")
    pr_t.showturtle()
    pr_t.penup()
    total_time_offset = offset + time_from_closest_low
    if -74 <= total_time_offset <= 74:
        y = (-130 + abs(total_time_offset) * (280/74))
        pr_t.goto(0, y)
    elif total_time_offset > 74 or total_time_offset < -74:
        y = (150 - abs(total_time_offset-74) * (280 / 74))
        pr_t.goto(0, y)
    else:
        print("Piankatank Align Error")


def piank_animation(counter, time_from_closest_low):
    '''
    One tide cycle is 12 hours, 25 minutes or 149, 5 minute periods.
    Taking away one 5 minute period to help account for process delays,
    that leaves 148 5 minute periods (counter values) for the animation
    '''
    pr = counter + (offset + time_from_closest_low)
    if 0 <= pr < 74:
        pr_t.seth(90)
        pr_t.fd(280 / 74)

    elif 74 <= pr < 148:
        pr_t.seth(270)
        pr_t.fd(280 / 74)

    elif 148 <= pr < 222:
        pr_t.seth(90)
        pr_t.fd(280 / 74)

    elif pr >= 222:
        pr_t.seth(270)
        pr_t.fd(280 / 74)

    elif pr < 0:
        pr_t.seth(270)
        pr_t.fd(280 / 74)

    else:
        print('Piankatank Animation Error')


def piank_slack_calc(counter, time_from_closest_low):
    pr = counter + (offset + time_from_closest_low)
    if 0 <= pr < 74:
        t = (73 - pr) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif 74 <= pr < 148:
        t = (147 - pr) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif 148 <= pr < 222:
        t = (221 - pr) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif pr >= 222:
        t = (295 - pr) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif pr < 0:
        t = (- pr) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    else:
        print("Piankatank Slack Calculation Error")

