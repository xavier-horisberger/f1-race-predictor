import pandas as pd

from src.processing.feature_engineering import previous_race_mean


def test_previous_race_mean_does_not_see_current_race():
    rows = pd.DataFrame({"driver_id": ["A", "A", "A"], "finish_position": [3, 5, 1]})
    values = previous_race_mean(rows, "driver_id", "finish_position", window=2)
    assert pd.isna(values.iloc[0])
    assert values.iloc[1] == 3
    assert values.iloc[2] == 4
