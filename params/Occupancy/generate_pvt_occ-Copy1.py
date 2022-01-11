import pandas as pd
import scipy.stats

class Generator:
    def __init__(self, path):
        self.plot_df_bus_freq = pd.read_csv(path)
        self.plot_df_bus_hist = []
        for i,row in self.plot_df_bus_freq.iterrows():
            freq = int(row['Freq'])
            for num in range(0,freq):
                self.plot_df_bus_hist.append(row['bus_main_data_mod'])

        self.plot_df_bus_series = pd.Series(self.plot_df_bus_hist)
        self.plot_df_bus_pdf = scipy.stats.gaussian_kde(self.plot_df_bus_series)

    def generate_bus_occ(self, n = 1000):
        return self.plot_df_bus_pdf.resample(n)

    