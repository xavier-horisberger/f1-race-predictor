"""FastF1 access helpers. No automatic downloads on import."""
from pathlib import Path


def enable_cache(cache_dir: str = "cache/fastf1") -> None:
    """Enable the local FastF1 cache for subsequent API calls."""
    import fastf1

    path = Path(cache_dir)
    path.mkdir(parents=True, exist_ok=True)
    fastf1.Cache.enable_cache(str(path))


def get_event_schedule(year: int):
    """Fetch a season's event schedule; requires an internet connection."""
    import fastf1

    enable_cache()
    return fastf1.get_event_schedule(year)
