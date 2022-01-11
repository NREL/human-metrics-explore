import pandas as pd
import scipy.stats

def generate_wb_fd(speed_dist_wb):
    wb_fd_list = []
    n = len(speed_dist_wb)
    for i in range(0,n):
        fd_temp = speed_dist_wb[i] * 1000/3600 * 2
        wb_fd_list.append(fd_temp)
        #print(randomlist)
        
    return(wb_fd_list)
