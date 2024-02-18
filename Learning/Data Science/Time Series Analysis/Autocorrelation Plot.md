![[Pasted image 20220918125614.png]]

An autocorrelation plot, often represented as an ACF (Autocorrelation Function) plot, ==visually displays the autocorrelation coefficients at different lags. This plot is helpful in identifying temporal patterns and understanding how each observation in a time series relates to its past values.==

The plot will show autocorrelation coefficients for different lags. ==Significant spikes away from the horizontal dashed line at 0 indicate the strength and direction of autocorrelation at those lags. This plot can be useful for identifying potential seasonality or patterns in the data.==

The ACF Plot can also help you determine the stationarity of TM.
- For a stationary Time Series, the ACF will drop to zero relatively quickly
	- while the ACF of non-stationary data decreases slowly.
- ACF is a plot of the autocorrelation of a time series.
- The auto correlation shows how the data is correlating across periods. 
- ==A value between 0 and 1, represents a positive correlation, and negative values would denote that the data is not correlated.==
- The autocorrelation function at lag-1 is the correlation between a time series and the same time series offset by one step.
- The plot shows ACF values at increasing/decreasing lags.
	- If these ==values are small and lie inside the blue shaded region, then they are not statistically significant.==
- The ACF Plot can help you determine the stationarity of TM.
- ==The ACF is measure of the linear predictability of the series. It is the Pearson correlation coefficient between to elements of a time series, e.g., at times s and t.==
- ==If the ACF and PACF plots demonstrate that the autocorrelation reaches and remains near zero, it will further support the argument that the differenced time series data resembles the white noise pattern and has become stationary without trend or seasonality. ==
- ACF should be a gradual decrease to towards zero, if sharp decrease 