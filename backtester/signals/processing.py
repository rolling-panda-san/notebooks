import pandas as pd

def as_freq(signal: pd.Series, freq: str, method: str = 'pad') -> pd.Series:
    """
    Resamples a signal to a specified frequency.

    Args:
        signal (pd.Series): The input signal.
        freq (str): The target frequency (e.g., 'ME' for monthly, 'W' for weekly).
        method (str): The resampling method ('pad' or 'ffill').

    Returns:
        pd.Series: The resampled signal.
    """
    if method == 'pad':
        return signal.resample(freq).ffill()
    else:
        return signal.resample(freq).apply(method)
