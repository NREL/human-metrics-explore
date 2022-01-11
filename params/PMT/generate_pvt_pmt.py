import pandas as pd
import scipy.stats

class Generator:
    def __init__(self, path):
        self.plot_df_pvt_pmt_freq = pd.read_csv(path)
        self.plot_df_pvt_pmt_hist = []
        for i,row in self.plot_df_pvt_pmt_freq.iterrows():
            freq = int(row['Freq'])
            for num in range(0,freq):
                self.plot_df_pvt_pmt_hist.append(row['private_PMT_vec'])

        self.plot_df_pvt_pmt_series = pd.Series(self.plot_df_pvt_pmt_hist)
        self.plot_df_pvt_pmt_pdf = scipy.stats.gaussian_kde(self.plot_df_pvt_pmt_series)

    def generate_pvt_pmt(self, n = 1000):
        return self.plot_df_pvt_pmt_pdf.resample(n)

    