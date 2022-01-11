import pandas as pd
import scipy.stats

def generate_pvt_fd(speed_dist_pvt):
    pvt_fd_list = []
    n = len(speed_dist_pvt)
    for i in range(0,n):
        fd_temp = speed_dist_pvt[i] * 1000/3600 * 2
        pvt_fd_list.append(fd_temp)
        #print(randomlist)
        
    return(pvt_fd_list)


    