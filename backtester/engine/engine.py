import pandas as pd
import os
from ..signals import TSMOM, VolatilityScale, as_freq

class BacktestEngine:
    """
    The core backtesting engine.
    """
    def __init__(self, strategy, instrument, signal, weighting):
        """
        Initializes the BacktestEngine.

        Args:
            strategy: The trading strategy.
            instrument: A list of instruments to trade.
            signal: The trading signal.
            weighting: The portfolio weighting scheme.
        """
        self.strategy = strategy
        self.instrument = instrument
        self.signal = signal
        self.weighting = weighting
        self.returns = None
        self.instrument_returns = None
        self.data = self._load_data()

    def _load_data(self):
        """
        Loads the historical data for the instruments.
        """
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        all_data = {}
        for ticker in self.instrument:
            file_path = os.path.join(data_dir, f"{ticker}.csv")
            if os.path.exists(file_path):
                all_data[ticker] = pd.read_csv(file_path, index_col=0, parse_dates=True)

        df = pd.concat(all_data, axis=1)
        df.columns = df.columns.droplevel(1) # drop the 'Adj Close' level
        return df

    def run(self):
        """
        Executes the backtest.
        """
        print("Running backtest...")
        instrument_returns = self.data.pct_change()

        # For now, we assume the signal is a list of signal objects
        # as in the notebook.
        if isinstance(self.signal, list):
            signals = []
            for s in self.signal:
                if isinstance(s, TSMOM):
                    # For TSMOM, we need to calculate the signal for each instrument
                    tsmom_signals = {}
                    for inst in self.instrument:
                        tsmom_signals[inst] = s.calculate(instrument_returns[inst])
                    signals.append(pd.concat(tsmom_signals, axis=1))
                elif isinstance(s, VolatilityScale):
                    # For VolatilityScale, we also calculate per instrument
                    vol_signals = {}
                    for inst in self.instrument:
                        vol_signals[inst] = s.calculate(instrument_returns[inst])
                    signals.append(pd.concat(vol_signals, axis=1))

            # Combine signals by multiplying them
            combined_signal = signals[0]
            for s in signals[1:]:
                combined_signal *= s
        else:
            combined_signal = self.signal.calculate(instrument_returns)

        # Resample signal to monthly
        combined_signal = as_freq(combined_signal, 'm', method='pad')

        # Calculate instrument returns based on signal
        self.instrument_returns = instrument_returns * combined_signal.shift(1)

        # For now, we assume equal weighting
        if self.weighting == "EQUAL_WEIGHT":
            weights = pd.DataFrame(1/len(self.instrument), index=self.instrument_returns.index, columns=self.instrument)
            self.returns = (self.instrument_returns * weights).sum(axis=1)

    def calculate_equity_curve(self, calculate_net=False, rebalance_freq='m'):
        """
        Calculates the portfolio equity curve.
        """
        print("Calculating equity curve...")
        return (1 + self.returns).cumprod()

    def get_return_by_instrument(self, calculate_net=False):
        """
        Gets returns for each instrument.
        """
        print("Getting return by instrument...")
        return self.instrument_returns
