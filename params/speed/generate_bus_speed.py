import pandas as pd
import scipy.stats
import random

def generate_bus_speed(n):
    bus_speed_list = []
    for i in range(0,n):
        speed_temp = random.uniform(15,30)
        bus_speed_list.append(speed_temp)
        #print(randomlist)
        
    return(bus_speed_list)
    