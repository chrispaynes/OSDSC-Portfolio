# Vocab
## Akaike Information Criterion (AIC) 
	- Auto arima is a brute-force method that tries different values of p and q while minimizing two criteria: AIC and BIC.
	- common metric to assess the regularized goodness-of-the-fit are:
	- These metrics provide measures of model performance that account for model complexity. AIC and BIC combine a term reflecting how well the model fits the data with a term that penalizes the model in proportion to its number of parameters [3].
	- As a regularization technique, we want to penalize based on the number of parameters in the model. Indeed, the larger p and q, the more lags you use to predict the next value, and the more likely you are to overfit your data.
## Auto Correlation Function ACF / MA / Moving Average
![[Pasted image 20220918125614.png]]
	- The ACF Plot can also help you determine the stationarity of TM.
	- For a stationary Time Series, the ACF will drop to zero relatively quickly
		- while the ACF of non-stationary data decreases slowly.
	- ACF is a plot of the autocorrelation of a time series.
	- The auto correlation shows how the data is correlating across periods. 
	- A value between 0 and 1, represents a positive correlation, and negative values would denote that the data is not correlated.
	- The autocorrelation function at lag-1 is the correlation between a time series and the same time series offset by one step.
	- The plot shows ACF values at increasing/decreasing lags.
		- If these values are small and lie inside the blue shaded region, then they are not statistically significant.
		- The ACF Plot can help you determine the stationarity of TM.
		- For a stationary Time Series, the ACF will drop to zero relatively quickly, while the ACF of non-stationary data decreases slowly.
	- The ACF is measure of the linear predictability of the series. It is the Pearson correlation coefficient between to elements of a time series, e.g., at times s and t.
	- If the ACF and PACF plots demonstrate that the autocorrelation reaches and remains near zero, it will further support the argument that the differenced time series data resembles the white noise pattern and has become stationary without trend or seasonality. 
	- ACF should be a gradual decrease to towards zero, if sharp decrease 

## Autocovariance
	- is simply the covariance between two elements in the series.
## AR (P)
	- ACF and PACF plots: After a time series has been stationarized by differencing, the next step in fitting an ARIMA model is to determine whether AR or MA terms are needed to correct any autocorrelation that remains in the differenced series. 
	- By looking at the autocorrelation function (ACF) and partial autocorrelation (PACF) plots of the differenced series, you can tentatively identify the numbers of AR and/or MA terms that are needed.
		- You are already familiar with the ACF plot: it is merely a bar chart of the coefficients of correlation between a time series and lags of itself.
		- The PACF plot is a plot of the partial correlation coefficients between the series and lags of itself.
		- use the value where the PACF plot reaches 1


## AR(1)
	-
## ARMA
	- ARMA model is simply the merger between AR(p) and MA(q) models:
	- AR(p) models try to explain the momentum and mean reversion effects often observed in trading markets.
	- MA(q) models try to capture the shock effects observed in the white noise terms. These shock effects could be thought of as unexpected events affecting the observation process e.g. Surprise earnings, wars, attacks, etc.
	- ARMA model attempts to capture both of these aspects when modeling financial time series. ARMA model does not take into account volatility clustering.

## ARIMA
	- The model requires a set of inputs to operate, where: 
		- p is the order of the autoregressive part specifically the lag of differencing series - AR
		- d is the degree of first differencing involved. 
		- q is the order of the moving average part specifically the lag of errors.  - MA
		- The value of d should be determined by the KPSS /ADFuller method. 
		- The values for the other variables can be automatically determined using the auto.arima function. 

## Augmented Dickey Fuller
	- Evaluate the stationarity of your time series data with Augmented Dickey-Fuller (ADFuler) test.
	- For ADFuller test, a p-value <= 0.05 allows us to reject the null hypothesis.
## Auto (prefix)
	- auto means itself
## Auto ARIMA
	- The auto_arima model is used to find the best model fit. It helps find the p, d, q.

## Autocorrelation
	- Autocorrelation is a mathematical representation of the degree of similarity between a given time series and a lagged version of itself over successive time intervals.
	- Autocorrelation measures a set of current values against a set of past values to see if they correlate (Dotis-Georgiou, 2021).
	- Also means that future values can be predicted as a linear function of past values.
	- In time series each observation called a lag could correlate with its prior lags (Educative, n.d).
	- Autocorrelation can be defined as a the correlation between itself and the other values of same variable(features) (in our case correlation between (Xt and Xt-1) (Xt and Xt-2). etc…) and it is denoted as ρ.
## Autocovariance
![[Pasted image 20220918130227.png]]
	- Autocovariance is defined as the covariance between the present value (xt) with the previous value (xt-1) and the present value (xt) with (xt-2). And it is denoted as ϒ.
	- Time series are typically characterized by some degree of serial dependence. This dependence can be measured by the autocovariance, which is simply the covariance between two elements in the series
## Autoregressive / Auto-Regressive / AR / (p)
	- AR(p) models try to explain the momentum and mean reversion effects often observed in trading markets.
	- In a multiple regression model, we forecast the variable of interest using a linear combination of predictors. In an autoregression model, we forecast the variable of interest using a linear combination of past values of the variable. The term autoregression indicates that it is a regression of the variable against itself.
	- is the order of the autoregressive part specifically the lag of differencing series
	- https://otexts.com/fpp2/AR.html#AR
	- this is the PACF value
## Bayesian information criterion (BIC)
	- Auto arima is a brute-force method that tries different values of p and q while minimizing two criteria: AIC and BIC.
	-  common metric to assess the regularized goodness-of-the-fit are:
	- These metrics provide measures of model performance that account for model complexity. AIC and BIC combine a term reflecting how well the model fits the data with a term that penalizes the model in proportion to its number of parameters [3].
	- As a regularization technique, we want to penalize based on the number of parameters in the model. Indeed, the larger p and q, the more lags you use to predict the next value, and the more likely you are to overfit your data.
## Correlation
	- Correlation is defined as how much increase(decrease) in one variable causes the other variable to increase(decrease) or vice-versa. 
## Correlation Coefficient
	- The correlation coefficient is a statistical measure of the strength of the relationship between the relative movements of two variables.
	- The values range between -1.0 and 1.0. A calculated number greater than 1.0 or less than -1.0 means that there was an error in the correlation measurement.
	- A correlation of -1.0 shows a perfect negative correlation, while a correlation of 1.0 shows a perfect positive correlation.
	- A correlation of 0.0 shows no linear relationship between the movement of the two variables.
## Covariance
	- Covariance is defined as the joint variance of two variables.
	- covariance is a measure of the joint variability of two random variables.[1]
	- If the greater values of one variable mainly correspond with the greater values of the other variable, and the same holds for the lesser values (that is, the variables tend to show similar behavior), the covariance is positive.[2]
	- In the opposite case, when the greater values of one variable mainly correspond to the lesser values of the other, (that is, the variables tend to show opposite behavior), the covariance is negative.
	- The sign of the covariance therefore shows the tendency in the linear relationship between the variables.
	- The magnitude of the covariance is not easy to interpret because it is not normalized and hence depends on the magnitudes of the variables.
	- The normalized version of the covariance, the correlation coefficient, however, shows by its magnitude the strength of the linear relation.
## Decomposition Models
	- https://online.stat.psu.edu/stat510/lesson/5/5.1
	- Decomposing Time Series means splitting Time Series  data into its 3 components: Trend, Seasonality, and Residual. It provides a visual summary of the components and helps detect the presence or the lack of these components . 
	- Decomposition procedures are used in time series to describe the trend and seasonal factors in a time series. More extensive decompositions might also include long-run cycles, holiday effects, day of week effects and so on. Here, we’ll only consider trend and seasonal decompositions.
	- One of the main objectives for a decomposition is to estimate seasonal effects that can be used to create and present seasonally adjusted values. A seasonally adjusted value removes the seasonal effect from a value so that trends can be seen more clearly. For instance, in many regions of the U.S. unemployment tends to decrease in the summer due to increased employment in agricultural areas. Thus a drop in the unemployment rate in June compared to May doesn’t necessarily indicate that there’s a trend toward lower unemployment in the country. To see whether there is a real trend, we should adjust for the fact that unemployment is always lower in June than in May.
## Differencing
	- Is a method of transforming time series to remove temporal dependence like trends and seasonality and helps stabilize the mean of the time series. 
	- It computes the differences between consecutive observations by subtracting the previous observation from the current observation (Brownlee, 2020).
	- In this time series data, only one order of difference is required to coerce stationarity.
	- Differencing can help stabilize the mean of a time series by removing changes in the level of a time series, and therefore eliminating (or reducing) trend and seasonality. 

## Lag
	- In time series each observation called a lag could correlate with its prior lags (Educative, n.d).  

## Ljung-Box statistics
	- The Ljung (pronounced Young) Box test (sometimes called the modified Box-Pierce, or just the Box test) is a way to test for the absence of serial autocorrelation, up to a specified lag k.
		-The test determines whether or not errors are iid (i.e. white noise) or whether there is something more behind them; whether or not the autocorrelations for the errors or residuals are non zero. Essentially, it is a test of lack of fit: if the autocorrelations of the residuals are very small, we say that the model doesn’t show ‘significant lack of fit’.
	- The Ljung–Box test may be defined as:
			- H0: The data are independently distributed (i.e. the correlations in the population from which the sample is taken are 0, so that any observed correlations in the data result from randomness of the sampling process).
			- Ha: The data are not independently distributed; they exhibit serial correlation.
## MA / Moving Average / (q)
	- ACF and PACF plots: After a time series has been stationarized by differencing, the next step in fitting an ARIMA model is to determine whether AR or MA terms are needed to correct any autocorrelation that remains in the differenced series. 
	- By looking at the autocorrelation function (ACF) and partial autocorrelation (PACF) plots of the differenced series, you can tentatively identify the numbers of AR and/or MA terms that are needed.
		- You are already familiar with the ACF plot: it is merely a bar chart of the coefficients of correlation between a time series and lags of itself.
		- The PACF plot is a plot of the partial correlation coefficients between the series and lags of itself.
	- MA(q) models try to capture the shock effects observed in the white noise terms. These shock effects could be thought of as unexpected events affecting the observation process e.g. Surprise earnings, wars, attacks, etc.

## Pvalue
- The _p_-value is a number, calculated from a [statistical test](https://www.scribbr.com/statistics/statistical-tests/), that describes how likely you are to have found a particular set of observations if the [null hypothesis](https://www.scribbr.com/statistics/null-and-alternative-hypotheses/) were true.
- _P_-values are used in [hypothesis testing](https://www.scribbr.com/statistics/hypothesis-testing/) to help decide whether to reject the null hypothesis.
- The smaller the _p_-value, the more likely you are to reject the null hypothesis.

## Partial Auto Correlation Function PACF
	![[Pasted image 20220918125501.png]]
	-  The partial autocorrelation (PACF) is the correlation between a time series and the lagged version of itself after we subtract the effect of correlation at smaller lags (Datacamp, nd)
	- In general, the "partial" correlation between two variables is the amount of correlation between them which is not explained by their mutual correlations with a specified set of other variables. For example, if we are regressing a variable Y on other variables X1, X2, and X3, the partial correlation between Y and X3 is the amount of correlation between Y and X3 that is not explained by their common correlations with X1 and X2. This partial correlation can be computed as the square root of the reduction in variance that is achieved by adding X3 to the regression of Y on X1 and X2.
	- A partial autocorrelation is the amount of correlation between a variable and a lag of itself that is not explained by correlations at all lower-order-lags. The autocorrelation of a time series Y at lag 1 is the coefficient of correlation between Yt and Yt-1, which is presumably also the correlation between Yt-1 and Yt-2. But if Yt is correlated with Yt-1, and Yt-1 is equally correlated with Yt-2, then we should also expect to find correlation between Yt and Yt-2. In fact, the amount of correlation we should expect at lag 2 is precisely the square of the lag-1 correlation. Thus, the correlation at lag 1 "propagates" to lag 2 and presumably to higher-order lags. The partial autocorrelation at lag 2 is therefore the difference between the actual correlation at lag 2 and the expected correlation due to the propagation of correlation at lag 1.
	- value maps to AR (p)
## Periodicity
	- the fact of something happening at regularly-spaced periods of time
	- A fundamental characteristic of time series data is how frequently the observations are spaced in time. How often the observations of a time series occur is called the sampling frequency or the periodicity of the series. For example, a time series with one observation each month has a monthly sampling frequency or monthly periodicity and so is called a monthly time series.
## Residuals
	- The residual of the decomposed time series is the time series after the trend and seasonality components are removed. 
	- The assumption that goes into time-series forecasting is that the residuals aren’t autocorrelated
## SARIMAX
## Seasonality
	- Seasonality refers to cycles that repeat regularly over time as shown below.
	- That cycle can be daily, weekly, monthly, quarterly, yearly, etc.
	- The cycle structure is considered seasonal if it repeats at the same frequency. 
	- The difference between seasonal and cyclical behavior has to do with how regular the period of change is.
	- A seasonal behavior is very strictly regular, meaning there is a precise amount of time between the peaks and troughs of the data.
		- For instance temperature would have a seasonal behavior. The coldest day of the year and the warmest day of the year may move (because of factors other than time than influence the data) but you will never see drift over time where eventually winter comes in June in the northern hemisphere.
	- Cyclical behavior on the other hand can drift over time because the time between periods isn't precise. For example, the stock market tends to cycle between periods of high and low values, but there is no set amount of time between those fluctuations.
## Sine Wave
	- A sine wave is a mathematical curve defined in terms of the sine trigonometric function, of which it is the graph.
	- It is a type of continuous wave and also a smooth periodic function.
	- A sine wave is a geometric waveform that oscillates (moves up, down, or side-to-side) periodically, and is defined by the function y = sin x. In other words, it is an s-shaped, smooth wave that oscillates above and below zero.
Sine waves are used in technical analysis and trading to help identify patterns and cross-overs related to oscillators.
## Spectral Density / Power Spectral Density / Power Spectrum
	- Spectra Density is a graph that shows frequencies related to the autocovariance time domain.
	- It represents the frequency domain of a time series and is directly related to the autocovariance time-domain representation.
	- The “frequency” is the number of observations before the seasonal pattern repeats.
	- Autocovariance is simply the covariance between two elements in the series.
	- Time Series sometimes shows periodic behavior which can be difficult to understand. So, you do Spectral analysis to discover underlying periodicities. 
		- You do so by transforming the data from the time domain to the frequency domain. 
		- The covariance of the time series can be represented by a function called spectral density, which is estimated using the squared correlation between the time series and sine/cosine waves at different frequencies spanned by the series (Jones, 2018).
		- Periodicity is the fact of something happening at regularly-spaced periods of time. An example of periodicity is the full moon happening every 29.5 days.
	- Interpretation of Spectral Density
			- In data science, periodicity is a pattern (trend) in a time series that occurs at regular time intervals.  If the time intervals at which the pattern repeats itself can't be precisely defined and are not constant the time series is said to be cyclical.
			- Power Spectral Density and Power Spectrum refer to the same thing – time and the variance between the previous and current time periods (covariance). This time signal is indicated on the Y-axis of the graph.
			- The X-axis represents the frequencies which are the number of observations before the seasonal pattern repeats.
			- When you transform the Power Spectral Density to the frequency, it shows a curve that is described as the spectral density.  
			- The Y-axis assigns value to the covariance between two elements (signals) in the series known as autocovariance. Please read more about the Y and X axes interpretation here.
	- In brief, the covariance of the time series can be represented by a function known as the spectral density. The spectral density can be estimated using on object known as a periodogram, which is the squared correlation between our time series and sine/cosine waves at the different frequencies spanned by the series (Venables & Ripley 2002).
	- For large n, the periodogram is approximately independent for distinct frequencies. This independence can be improved – as can the visual quality and interpretability of the plot – by smoothing the periodogram using a kernel smoother (which is generally some sort of weighted running average).



## Stationarity
	- is an assumption in Time Series that that the mean, variance and autocorrelation structure do not change over time (Sematech, Sangarshanan, 2018).
	- It means that the distribution of the data does not change with time.
	- <b>For Time Series to be stationary it must fulfill these three criteria:</b> 
		- The series has zero trends, it is not growing or shrinking.
		- The variance is constant.
		- The autocorrelation is constant. How each value in the time series is related to its neighbors stay the same (Datacamp, n.d).
	- Stationarity of the time series data should be established prior to modeling.
	- You can use the Kwiatkowski-PhillipsSchmidt-Shin (KPSS) test or ADFuller test. 

## Trend
	- The trend of a time series can be determined by analyzing the overall direction of the series over a period. It can be upward or downward. 

## White Noise
	- The concept of white noise is essential for time series analysis and forecasting. In the most simple words, white noise tells you if you should further optimize the model or not.
	- White noise is a series that’s not predictable, as it’s a sequence of random numbers. If you build a model and its residuals (the difference between predicted and actual) values look like white noise, then you know you did everything to make the model as good as possible. On the opposite side, there’s a better model for your dataset if there are visible patterns in the residuals.
	- The following conditions must be satisfied for a time series to be classified as white noise:
		- The average value (mean) is zero
		- Standard deviation is constant — it doesn’t change over time
		- The correlation between time series and its lagged version is not significant
	- There are three (easy) ways to test if time series resembles white noise:
		- By plotting the time series
		- By comparing mean and standard deviation over time
		- By examining autocorrelation plots