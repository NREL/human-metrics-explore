import pandas as pd
import scipy.stats
import random

def generate_pvt_speed(n):
    pvt_speed_list = []
    for i in range(0,n):
        speed_temp = random.uniform(25,100)
        pvt_speed_list.append(speed_temp)
        #print(randomlist)
        
    return(pvt_speed_list)
    