import pandas as pd
import numpy as np

class TSMOM:
    """
    Time-series momentum signal.
    """
    def __init__(self, lookback: int = 252, shift: int = 2):
        """
        Initializes the TSMOM signal.

        Args:
            lookback (int): The lookback period for calculating the momentum.
            shift (int): The number of periods to shift the signal.
        """
        self.lookback = lookback
        self.shift = shift

    def calculate(self, instrument_return: pd.Series) -> pd.Series:
        """
        Calculates the time-series momentum signal.

        Args:
            instrument_return (pd.Series): A pandas Series of instrument returns.

        Returns:
            pd.Series: A pandas Series of the calculated signal.
        """
        signal = instrument_return.rolling(self.lookback).sum().fillna(0).pipe(np.sign).shift(self.shift)
        return signal

class VolatilityScale:
    """
    Volatility scaling signal.
    """
    def __init__(self, target_volatility: float = 0.4, ann_factor: int = 261, com: int = 60, signal_cap: float = 0.95):
        """
        Initializes the VolatilityScale signal.

        Args:
            target_volatility (float): The target annualized volatility.
            ann_factor (int): The annualization factor.
            com (int): The center of mass for the exponentially weighted moving average.
            signal_cap (float): The cap for the volatility scaling signal.
        """
        self.target_volatility = target_volatility
        self.ann_factor = ann_factor
        self.com = com
        self.signal_cap = signal_cap

    def calculate(self, instrument_return: pd.Series) -> pd.Series:
        """
        Calculates the volatility-scaled signal.

        Args:
            instrument_return (pd.Series): A pandas Series of instrument returns.

        Returns:
            pd.Series: A pandas Series of the calculated volatility-scaled signal.
        """
        vol = instrument_return.ewm(com=self.com).std() * np.sqrt(self.ann_factor)
        signal = self.target_volatility / vol
        signal[signal > signal.quantile(self.signal_cap)] = signal.quantile(self.signal_cap)
        return signal
