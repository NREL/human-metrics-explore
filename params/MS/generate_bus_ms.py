import pandas as pd
import scipy.stats

class Generator:
    def __init__(self, path):
        self.plot_df_bus_ms_freq = pd.read_csv(path)
        self.plot_df_bus_ms_hist = []
        for i,row in self.plot_df_bus_ms_freq.iterrows():
            freq = int(row['Freq'])
            for num in range(0,freq):
                self.plot_df_bus_ms_hist.append(row['bus_vec'])

        self.plot_df_bus_ms_series = pd.Series(self.plot_df_bus_ms_hist)
        self.plot_df_bus_ms_pdf = scipy.stats.gaussian_kde(self.plot_df_bus_ms_series)

    def generate_bus_ms(self, n = 1000):
        return self.plot_df_bus_ms_pdf.resample(n)

    