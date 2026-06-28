import pandas as pd
import numpy as np
from scipy import stats

def load_data(filename):
    return pd.read_csv(filename)

def calculate_statistics(df):
    return {
        'mean_cases': df['cases'].mean(),
        'std_dev': df['cases'].std(),
        'median': df['cases'].median(),
    }

def trend_analysis(df):
    x = np.arange(len(df))
    y = df['cases'].values
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return {
        'slope': slope,
        'r_squared': r_value ** 2,
        'trend': 'increasing' if slope > 0 else 'decreasing'
    }
