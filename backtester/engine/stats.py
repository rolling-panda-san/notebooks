import pandas as pd
import numpy as np
from enum import Enum

class PerfStats(Enum):
    CAGR = "CAGR"
    ANN_VOL = "Annualised vol"
    SHARPE = "Sharpe ratio"
    MAX_DD = "Max drawdown"
    CALMAR = "Calmar ratio"
    SKEW = "Skewness"
    KURT = "Kurtosis"
    WORST_RETURN = "Worst return"
    WORST_1D_RETURN = "Worst 1d return"
    WORST_1W_RETURN = "Worst 1w return"
    WORST_1M_RETURN = "Worst 1m return"

class Performance:
    """
    Calculates and displays key performance metrics.
    """
    def __init__(self, returns: pd.Series, return_type='cum'):
        if return_type == 'cum':
            self.returns = returns.pct_change().fillna(0)
        else:
            self.returns = returns
        self.equity_curve = (1 + self.returns).cumprod()

    def cagr(self):
        return self.equity_curve.iloc[-1] ** (252 / len(self.equity_curve)) - 1

    def ann_vol(self):
        return self.returns.std() * np.sqrt(252)

    def sharpe_ratio(self):
        return self.cagr() / self.ann_vol()

    def max_drawdown(self):
        return (self.equity_curve / self.equity_curve.cummax() - 1).min()

    def calmar_ratio(self):
        return self.cagr() / abs(self.max_drawdown())

    def skewness(self):
        return self.returns.skew()

    def kurtosis(self):
        return self.returns.kurtosis()

    def summary(self):
        """
        Returns a DataFrame with the performance summary.
        """
        summary_data = {
            PerfStats.CAGR.value: self.cagr(),
            PerfStats.ANN_VOL.value: self.ann_vol(),
            PerfStats.SHARPE.value: self.sharpe_ratio(),
            PerfStats.MAX_DD.value: self.max_drawdown(),
            PerfStats.CALMAR.value: self.calmar_ratio(),
            PerfStats.SKEW.value: self.skewness(),
            PerfStats.KURT.value: self.kurtosis(),
            PerfStats.WORST_RETURN.value: self.returns.min(),
            PerfStats.WORST_1D_RETURN.value: self.returns.min(),
            PerfStats.WORST_1W_RETURN.value: self.returns.resample('W').sum().min(),
            PerfStats.WORST_1M_RETURN.value: self.returns.resample('M').sum().min(),
        }

        # Check if the input is a Series or DataFrame
        if isinstance(self.returns, pd.Series):
            return pd.Series(summary_data, name=self.returns.name)
        else: # It's a DataFrame
            # This part needs to be adapted if we want to calculate stats for multiple columns
            # For now, we'll just return it for the first column
            return pd.DataFrame(summary_data, index=[self.returns.columns[0]]).T
