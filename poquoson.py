#This module determines current tide height for animation and timedelta purposes at Plum Island on the Poquoson River
#This is the clock from which the others are offset from (offset = 0)

import turtle
import datetime
import time

p_t = turtle.Turtle()
# p_t represents the Poquoson tide high and direction
offset = 0

def poq_align(time_from_closest_low):
    p_t.color("cyan")
    p_t.showturtle()
    p_t.penup()
    total_time_offset = offset + time_from_closest_low
    if -74 <= total_time_offset <= 74:
        y = (-130 + abs(total_time_offset) * (280/74))
        p_t.goto(400, y)
    elif total_time_offset > 74 or total_time_offset < -74:
        y = (150 - abs(total_time_offset-74) * (280 / 74))
        p_t.goto(400, y)
    else:
        print("Poquoson Align Error")


def poq_animation(counter, time_from_closest_low):
    '''
    One tide cycle is 12 hours, 25 minutes or 149, 5 minute periods.
    Taking away one 5 minute period to help account for process delays,
    that leaves 148 5 minute periods (counter values) for the animation
    '''
    p = counter + (offset + time_from_closest_low)
    if 0 <= p < 74:
        p_t.seth(90)
        p_t.fd(280 / 74)

    elif 74 <= p < 148:
        p_t.seth(270)
        p_t.fd(280 / 74)

    elif 148 <= p < 222:
        p_t.seth(90)
        p_t.fd(280 / 74)

    elif p >= 222:
        p_t.seth(270)
        p_t.fd(280 / 74)

    elif p < 0:
        p_t.seth(270)
        p_t.fd(280 / 74)

    else:
        print('Poquoson Animation Error')


def poq_slack_calc(counter, time_from_closest_low):
    p = counter + (offset + time_from_closest_low)
    if 0 <= p < 74:
        t = (73 - p) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif 74 <= p < 148:
        t = (147 - p) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif 148 <= p < 222:
        t = (221 - p) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif p >= 222:
        t = (295 - p) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    elif p < 0:
        t = (- p) * (5 * 60)
        slack_time = datetime.timedelta(seconds=t)
        time_output = time.strptime(str(slack_time), "%H:%M:%S")
        time_print = time.strftime("%H hr %M min", time_output)
        return time_print

    else:
        print("James Slack Calculation Error")
