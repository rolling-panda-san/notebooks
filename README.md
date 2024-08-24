# Analysis on systematic trading strategies

## What is this repo?

This repository documents researches on

- Systematic trading strategies (mainly using futures at the moment) that are published in the academic space
- Some other miscellaneous results

The purpose is to reproduce what are presented in the papers, update the results on a regular basis and potentially add
further experiments. Notebooks are automatically pushed to github.

** Throughout the notebooks, an internal library called `vivace` is used to facilitate the data management and quantitative analysis. 
This library will remain private as it's proprietary. **

## What are the contents?

Currently, it maintains the following trading strategies

| Strategy name                                | Main reference                | Asset class                         | Notebook                                          |
|----------------------------------------------|-------------------------------|-------------------------------------|---------------------------------------------------|
| Time-series momentum                         | Moskowitz 2012                | Equity, Fixed-income, FX, Commodity | `trend_following_moskowitz2012.ipynb`             |
| Time-series momentum                         | Baltas 2020                   | Equity, Fixed-income, FX, Commodity | `trend_following_baltas2020.ipynb`                |
| Time-series momentum with breakout signal    | Chevallier and Ielpo 2014 etc | Equity, Fixed-income, FX, Commodity | `trend_following_breakout.ipynb`                  |
| FX carry                                     | Deutsche Bank 2009            | FX                                  | `fx_carry.ipynb`                                  |
| Commodity term structure                     | Koijen 2018 etc               | Commodity                           | `commodity_term_structure.ipynb`                  |
| Commodity momentum                           | Asness 2013 etc               | Commodity                           | `commodity_momentum.ipynb`                        |
| Commodity skewness                           | Fernandez-Perez 2018 etc      | Commodity                           | `commodity_skewness.ipynb`                        |
| Commodity intra-curve                        | La Française Group 2015       | Commodity                           | `commodity_intra_curve.ipynb`                     |
| Commodity crush spread mean-reversion        | Simon 1999                    | Commodity                           | `commodity_crush_spread_stat_arb.ipynb`           |
| Commodity crack spread mean-reversion        | Girma and Paulson 1999        | Commodity                           | `commodity_crack_spread_stat_arb.ipynb`           |
| Commodity basis momentum                     | Boons 2019                    | Commodity                           | `commodity_basis_momentum.ipynb`                  |
| Commodity trend following in Chinese futures | Zhang and Zhou 2017           | Commodity                           | `commodity_trend_following_chinese_futures.ipynb` |
| Cross-asset skewness                         | Baltas 2019 etc               | Equity, Fixed-income, FX, Commodity | `cross_asset_skewness.ipynb`                      |
| Equity overnight returns                     | Knuteson 2020 etc             | Equity                              | `overnight_returns.ipynb`                         |
| Equity short-term trading                    | Connors 2009                  | Equity                              | `equity_short_term_trading_connors.ipynb`         |
| ETF intraday momentum                        | Gao 2018                      | Equity                              | `equity_etf_intraday_momentum.ipynb`              |

Additionally, there are notebooks on the following topics:

| Analysis                                   | Main reference | Asset Class                         | Notebook                          |
|--------------------------------------------|----------------|-------------------------------------|-----------------------------------|
| Long-only performance on futures contracts | -              | Equity, Fixed-income, FX, Commodity | `futures_long_only.ipynb`         |
| Actively traded contract months            | -              | Equity, Fixed-income, FX, Commodity | `futures_active_contracts.ipynb`  |
| Greeks under Normal Black-Scholes model    | -              | -                                   | `Greeks_under_normal_model.ipynb` |
| Realised volatility measures               | Santander 2012 | Equity, Fixed-income, FX, Commodity | `realised_volatility.ipynb`       |
| Inverse options                            | Alexander 2021 | Crypto                              | `inverse_option.ipynb`            |
| Uniswap V2 liquidity pool yield            | -              | Crypto                              | `crypto_uniswap_graph.ipynb`      |

# Reference

- Alexander, C. and Imeraj, A., 2021. Inverse Options in a Black-Scholes World. arXiv preprint arXiv:2107.12041.
- Asness, C.S., Moskowitz, T.J. and Pedersen, L.H., 2013. Value and momentum everywhere. The Journal of Finance, 68(3),
  pp.929-985.
- Bakshi, G., Gao, X. and Rossi, A.G., 2019. Understanding the sources of risk underlying the cross section of commodity
  returns. Management Science, 65(2), pp.619-641.
- Baltas, N. and Kosowski, R., 2020. Demystifying time-series momentum strategies: Volatility estimators, trading rules
  and pairwise correlations. Market Momentum: Theory and Practice", Wiley.
- Baltas, N. and Salinas, G., 2019. Cross-Asset Skew. Available at SSRN.
- BCOM Methodology - Bloomberg Professional Services https://assets.bbhub.io/professional/sites/10/BCOM-Methodology-MAR-2022_FINAL.pdf
- Boons, M. and Prado, M.P., 2019. Basis momentum. The Journal of Finance, 74(1), pp.239-279.
- Chevallier, J. and Ielpo, F., 2014. “Time series momentum” in commodity markets. Managerial Finance.
- Connors, L.A. and Alvarez, C., 2009. Short Term Trading Strategies that Work: A Quantified Guide to Trading Stocks and
  ETFs. TradingMarkets Publishing Group.
- Deutsche Bank, 2009, db Currency Return.
- Fernandez-Perez, A., Frijns, B., Fuertes, A.M. and Miffre, J., 2018. The skewness of commodity futures returns.
  Journal of Banking & Finance, 86, pp.143-158.
- Gao, L., Han, Y., Li, S.Z. and Zhou, G., 2018. Market intraday momentum. Journal of Financial Economics, 129(2),
  pp.394-414.
- Girma, P.B. and Paulson, A.S., 1999. Risk arbitrage opportunities in petroleum futures spreads. Journal of Futures
  Markets, 19(8), pp.931-955.
- Hollstein, F., Prokopczuk, M. and Tharann, B., 2020. Anomalies in commodity futures markets: Risk or mispricing?.
  Available at SSRN
- Knuteson, B., 2020. Strikingly Suspicious Overnight and Intraday Returns. arXiv preprint arXiv:2010.01727.
- Koijen, R.S., Moskowitz, T.J., Pedersen, L.H. and Vrugt, E.B., 2018. Carry. Journal of Financial Economics, 127(2),
  pp.197-225.
- La Française Group, 2015, Commodity premia: It’s all about risk control
- Li, B., Zhang, D. and Zhou, Y., 2017. Do trend following strategies work in Chinese futures markets?. Journal of Futures Markets, 37(12), pp.1226-1254.
- Moskowitz, T.J., Ooi, Y.H. and Pedersen, L.H., 2012. Time series momentum. Journal of financial economics, 104(2),
  pp.228-250.
- Santander, 2012, Measuring Historical Volatility.
- Simon, D.P., 1999. The soybean crush spread: Empirical evidence and trading strategies. Journal of Futures Markets:
  Futures, Options, and Other Derivative Products, 19(3), pp.271-289.
