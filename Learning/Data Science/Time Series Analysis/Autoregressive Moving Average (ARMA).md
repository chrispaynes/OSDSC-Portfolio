An Autoregressive Moving Average (ARMA) model is a ==statistical time series model that combines autoregressive (AR) and moving average (MA) components to capture the temporal dependencies and patterns within a time series.== 

The ARMA model is ==part of a broader class of models known as ARIMA (Autoregressive Integrated Moving Average), which also includes differencing to handle non-stationary time series.== ARMA models are widely used in time series analysis for forecasting and understanding the underlying structure of sequential data.

The autoregressive component in an ARMA model represents the linear dependence of the current value on its past values. The order of the autoregressive component, denoted as $p$, specifies the number of lagged terms used in the model.

On the other hand, the moving average component captures the linear dependence on past white noise or random shocks. The order of the moving average component, denoted as $q$, indicates the number of lagged shocks included in the model.

Mathematically, an $ARMA(p, q)$ model can be expressed as:

$X_t = c + \phi_1X_{t-1} + \phi_2X_{t-2} + \ldots + \phi_pX_{t-p} + \varepsilon_t - \theta_1\varepsilon_{t-1} - \theta_2\varepsilon_{t-2} - \ldots - \theta_q\varepsilon_{t-q}$

Here, $X_t$ is the time series variable at time $t$, $c$ is a constant, $\phi_i$ are the autoregressive coefficients, $\varepsilon_t$ are white noise errors at time $t$, and $\theta_j$ are the moving average coefficients.

==ARMA models are employed when the underlying time series exhibits both autoregressive and moving average characteristics, and the model parameters are estimated to capture the observed patterns and dependencies in the data.==


- AR(p) models try to explain the momentum and mean reversion effects often observed in trading markets.
- MA(q) models try to capture the shock effects observed in the white noise terms. These shock effects could be thought of as unexpected events affecting the observation process e.g. Surprise earnings, wars, attacks, etc.