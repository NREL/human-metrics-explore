import pandas as pd
import scipy.stats
import random

def generate_wb_lm(n):
    wb_lm_list = []
    for i in range(0,n):
        lm_temp = random.uniform(1,2)
        wb_lm_list.append(lm_temp)
        #print(randomlist)
        
    return(wb_lm_list)