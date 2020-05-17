#Testing module

import turtle
import time
import initial_graphics
import weather_values
import james_river
import piankatank_river
import poquoson
import r_weather
import pr_weather
import p_weather

#Macbook Pro window default display resolution: 1280 x 800

'''
'time_from_closest_low' allows setting of the clock even when the current time does not match up with 
the actual low of the default clock. The number input should be the number of 5 minute increments to or from
the closest low, with future times being represented as negative values. Poquoson is currently the default tide clock
'''
def run_tide():

    time_from_closest_low = -7

    initial_graphics.win_open()
    initial_graphics.tide_scale()
    weather_values.weather_info()

    '''
    The 'delta' represents one 5 minute period removed from th tide clock to account for process lag times. Any lag time over
    the given timer in the inner while loop will be subtracted from 'delta' to tell the program how long to sleep before 
    restarting so as to recalibrate the clock each tide cycle
    '''
    delta = 300       #initially set to 300 seconds as to not cuase a delay when starting the clock

    while True:

        timeout = 44400
        counter = 0         #each counter increment of 1 represents the passing of a 5 minute period
        animation_start_time = time.perf_counter()
        delay = 300 - delta      #clock recalibration value
        time.sleep(delay)        #clock recalibration
        james_river.james_align(time_from_closest_low)
        piankatank_river.piank_align(time_from_closest_low)
        poquoson.poq_align(time_from_closest_low)
        weather_values.weather_update(r_weather.rich_weath(), pr_weather.pr_weath(), p_weather.poq_weath())
        weather_values.wind_update(r_weather.rich_wind(), pr_weather.pr_wind(), p_weather.poq_wind())


        while time.perf_counter() < animation_start_time + timeout:

            james_river.james_animation(counter, time_from_closest_low)
            piankatank_river.piank_animation(counter, time_from_closest_low)
            poquoson.poq_animation(counter, time_from_closest_low)
            weather_values.slack_update(james_river.james_slack_calc(counter, time_from_closest_low), piankatank_river.piank_slack_calc(counter, time_from_closest_low), poquoson.poq_slack_calc(counter, time_from_closest_low))
            time.sleep(300)
            counter += 1

        animation_end_time = time.perf_counter()
        delta = ((animation_end_time - animation_start_time) - timeout)

        if delta > 300:
            print("Excess process time of" + str(delta))


        turtle.mainloop()


if __name__ == "__main__":
    run_tide()
    


