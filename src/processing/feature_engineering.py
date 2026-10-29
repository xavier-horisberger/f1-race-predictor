"""Feature calculations must exclude the race being predicted."""
import pandas as pd


def previous_race_mean(
    rows: pd.DataFrame,
    entity_column: str,
    value_column: str,
    window: int = 5,
) -> pd.Series:
    """Rolling mean of previous rows for each entity in chronological order.

    Caller must sort by race date (and race identifier) first. This helper is
    intended for one record per entity and GP; otherwise aggregate first.
    """
    return rows.groupby(entity_column, sort=False)[value_column].transform(
        lambda s: s.shift(1).rolling(window=window, min_periods=1).mean()
    )
