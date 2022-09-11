import researchpy as rp
import scipy.stats as stats
from coalas import csvReader as c
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv('PerInc.csv')
   # df = pd.read_csv('test.csv')
    print(df.head())
#    des, res = rp.ttest(df['num'], df['neg']) 
    re = stats.pearsonr(df['Price'], df['TransactionsVolume'])
#    print(res)
    print(re)