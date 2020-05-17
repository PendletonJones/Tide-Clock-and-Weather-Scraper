# Tide-Clock-and-Weather-Scraper

An application to keep tide times and scrape current weather for specific locations. 

The clock itself is based on the lunar day 24 hr 50 minutes, and one clock can be set at anytime by knowing the time distance between
the current time, and the time of the known closest low tide at that location. The other clock locations are then set as offsets of that
first clock, so a single iterative counter can be used for animation and timedelta purposes. 

The Open Weather Map API is used to request weather data for the Lat Long of the desired location. Due to request lag times, the weather
is currently only called every tide cycle (outer while loop). The next update will include another file to which the weather values are 
written, eliminating the requirement for the 'main.py' program to call the requests itself. 

Based on high processor usage of having this on an ifinite loop, probably needs to be reconfigured with a crontab and sit on an API server instead of as an ever running script on my computer. 


