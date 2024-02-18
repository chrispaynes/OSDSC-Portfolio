Here are common ways to assess the quality of a time series model:

1. **Visual Inspection:**
   - Begin by visually inspecting the time series plot, including the fitted values and residuals. Look for trends, seasonality, and any remaining patterns that the model might have missed.

2. **Residual Analysis:**
   - Examine the residuals (the differences between observed and predicted values) for randomness. Residuals should ideally be independent, follow a normal distribution, and exhibit constant variance over time. Plotting the residuals against time or model predictions can help identify any patterns or trends.

3. **Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF):**
   - Analyze the ACF and PACF of the residuals. Significant autocorrelation at certain lags may indicate that the model has not adequately captured temporal dependencies.

4. **Ljung-Box Test:**
   - Perform the Ljung-Box test on the residuals to formally test for significant autocorrelation at different lags. Rejection of the null hypothesis suggests inadequacies in the model.

5. **Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE):**
   - Calculate these metrics to quantify the accuracy of the model's predictions. Lower values indicate better model performance.

6. **Forecast Accuracy Metrics:**
   - Evaluate forecast accuracy using metrics such as Mean Absolute Percentage Error (MAPE), Symmetric Mean Absolute Percentage Error (sMAPE), or Forecast Bias. These metrics provide insights into how well the model predicts future values.

7. **Information Criteria:**
   - Use information criteria such as Akaike Information Criterion (AIC) or Bayesian Information Criterion (BIC) to compare different models. Lower values indicate a better balance between model fit and complexity.

8. **Out-of-Sample Testing:**
   - Reserve a portion of the data for out-of-sample testing to assess how well the model generalizes to new observations. Compare the model's predictions with actual values in the out-of-sample period.

9. **Cross-Validation:**
   - Perform cross-validation by splitting the data into multiple training and testing sets. Evaluate the model's performance across different folds to ensure consistency.

10. **Domain Expertise:**
    - Consult domain experts to validate whether the model's predictions align with known patterns and expectations in the data.

By combining these methods, analysts can gain a comprehensive understanding of a time series model's quality and make informed decisions about its suitability for forecasting or analysis.