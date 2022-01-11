import numpy as np
import pandas as pd
import scipy.stats


class Generator:
    def __init__(self, mode):
        ###no of iterations
        n = 10000

        ###assign values

        ####speed
        if mode == "wb":
            l_speed = 4
            u_speed = 20
        elif mode == "bus":
            l_speed = 20
            u_speed = 40
        elif mode == "pvt":
            l_speed = 20
            u_speed = 80

        speed_dist = np.random.uniform(l_speed,u_speed,n)
        self.speed_series = pd.Series(speed_dist)
        self.speed_pdf = scipy.stats.gaussian_kde(self.speed_series)

    def generate(self, n = 1000):
        return self.speed_pdf.resample(n)
