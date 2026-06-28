import pandas as pd
from covid_analysis.analyze import calculate_statistics

def test_calculate_statistics():
    df = pd.DataFrame({'cases': [10, 20, 30, 40, 50]})
    stats = calculate_statistics(df)
    assert stats['mean_cases'] == 30.0
    assert stats['median'] == 30.0
