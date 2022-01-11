import pandas as pd
import scipy.stats

class Generator:
    def __init__(self, path):
        self.plot_df_pvt_freq = pd.read_csv(path)
        self.plot_df_pvt_hist = []
        for i,row in self.plot_df_pvt_freq.iterrows():
            freq = int(row['Freq'])
            for num in range(0,freq):
                self.plot_df_pvt_hist.append(row['pvt_occ_means_vec'])

        self.plot_df_pvt_series = pd.Series(self.plot_df_pvt_hist)
        self.plot_df_pvt_pdf = scipy.stats.gaussian_kde(self.plot_df_pvt_series)

    def generate_pvt_occ(self, n = 1000):
        return self.plot_df_pvt_pdf.resample(n)

    