import pandas as pd
import scipy.stats
import random

def generate_bus_lm(n):
    bus_lm_list = []
    for i in range(0,n):
        lm_temp = random.uniform(10,20)
        bus_lm_list.append(lm_temp)
        #print(randomlist)
        
    return(bus_lm_list)