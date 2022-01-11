import pandas as pd
import scipy.stats

def generate_bus_fd(speed_dist_bus):
    bus_fd_list = []
    n = len(speed_dist_bus)
    for i in range(0,n):
        fd_temp = speed_dist_bus[i] * 1000/3600 * 2
        bus_fd_list.append(fd_temp)
        #print(randomlist)
        
    return(bus_fd_list)

    