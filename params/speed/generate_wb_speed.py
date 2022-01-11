import pandas as pd
import scipy.stats
import random

def generate_wb_speed(n):
    wb_speed_list = []
    for i in range(0,n):
        speed_temp = random.uniform(5,20)
        wb_speed_list.append(speed_temp)
        #print(randomlist)
        
    return(wb_speed_list)
    