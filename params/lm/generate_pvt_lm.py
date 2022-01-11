import pandas as pd
import scipy.stats
import random

def generate_pvt_lm(n):
    pvt_lm_list = []
    for i in range(0,n):
        lm_temp = random.uniform(4,6)
        pvt_lm_list.append(lm_temp)
        #print(randomlist)
        
    return(pvt_lm_list)