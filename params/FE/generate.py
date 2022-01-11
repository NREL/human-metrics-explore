import pandas as pd
import scipy.stats

class Generator:
    def __init__(self, path):
        self.FE_df = pd.read_csv(path)
        self.FE_hist = []
        for i,row in self.FE_df.iterrows():
            freq = int(row['freq'])
            for num in range(0,freq):
                self.FE_hist.append(row['kpl'])

        self.FE_series = pd.Series(self.FE_hist)
        self.FE_pdf = scipy.stats.gaussian_kde(self.FE_series)

    def generate(self, n = 1000):
        return self.FE_pdf.resample(n)
