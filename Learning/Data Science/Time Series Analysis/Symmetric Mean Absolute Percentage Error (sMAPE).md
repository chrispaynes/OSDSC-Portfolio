Symmetric Mean Absolute Percentage Error (sMAPE) is ==a metric commonly used to evaluate the accuracy of forecasting models, particularly in the context of time series analysis. It is a symmetric and percentage-based metric designed to measure the relative accuracy of predicted values compared to actual values. The symmetrical nature of sMAPE addresses the issue of scale, making it suitable for comparing forecast performance across different datasets.==

The formula for calculating sMAPE is:

$sMAPE = \frac{1}{n} \sum_{t=1}^{n} \frac{|Y_t - \hat{Y}_t|}{(|Y_t| + |\hat{Y}_t|)/2} \times 100\%$

where:
- $Y_t$ is the actual value at time $t$,
- $\hat{Y}_t$ is the predicted value at time $t$,
- $n$ is the total number of observations.

==The key feature of sMAPE is that it symmetrically penalizes both overestimation and underestimation errors, providing a balanced measure of forecast accuracy. The result is expressed as a percentage, making it interpretable and comparable across different datasets.==

While sMAPE is a widely used metric, it is essential to consider its limitations. Specifically, ==sMAPE can produce infinite values when the actual values are zero, and care should be taken in interpreting results when dealing with datasets containing zero values.== Overall, sMAPE is a valuable tool for assessing the relative accuracy of forecasting models and is commonly employed in various industries, including finance, supply chain, and energy forecasting.