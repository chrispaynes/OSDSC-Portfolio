![[Pasted image 20230916173758.png|500]]
The Weibull distribution is a continuous probability distribution used to model the time until an event occurs. It is named after Wallodi Weibull, who introduced it in the mid-20th century. The Weibull distribution is versatile and can take on various shapes, making it useful for modeling a wide range of phenomena, including reliability and survival data.

Key characteristics of the Weibull distribution include:

1. **Probability Density Function (PDF)**:
   - The probability density function of the Weibull distribution is given by:
     ```
     f(x; λ, k) = (k/λ) * (x/λ)^(k-1) * e^(-(x/λ)^k) for x >= 0
     ```
     where:
     - `x` is the random variable representing the time-to-event or survival time.
     - `λ` (lambda) is the scale parameter, which determines the scale or location of the distribution.
     - `k` (kappa) is the shape parameter, which controls the shape of the distribution.
     - The distribution is defined for `x >= 0`.

2. **Shape Parameter (k)**:
   - The shape parameter, `k`, influences the shape of the Weibull distribution.
     - When `k` is less than 1, the distribution is decreasing, indicating a higher probability of early failures (e.g., infant mortality in reliability analysis).
     - When `k` is equal to 1, the distribution becomes the exponential distribution.
     - When `k` is greater than 1, the distribution is increasing, indicating a higher probability of later failures (e.g., wear-out failures in reliability analysis).
   - The value of `k` determines whether the distribution is right-skewed (k > 1) or left-skewed (k < 1).

3. **Scale Parameter (λ)**:
   - The scale parameter, `λ`, determines the scale or location of the distribution along the x-axis. It influences the average or median time until the event.

4. **Mean and Variance**:
   - The mean of the Weibull distribution is given by `λ * Γ(1 + 1/k)`, where Γ is the gamma function.
   - The variance is given by `λ^2 * [Γ(1 + 2/k) - (Γ(1 + 1/k))^2]`.

5. **Applications**:
   - The Weibull distribution is commonly used in reliability engineering to model the distribution of lifetimes of components or systems. It can describe the failure behavior of mechanical and electronic components, as well as the distribution of survival times in medical studies.
   - It is also used in various other fields, including finance (modeling market crashes), environmental science (modeling environmental data), and wind energy (modeling wind speeds).

6. **Probability of Survival**:
   - The Weibull distribution is often used to calculate the probability of survival beyond a certain time. The survival function, denoted as `S(x)`, is given by `S(x) = e^(-(x/λ)^k)`.

The Weibull distribution's flexibility in capturing various shapes of data makes it a valuable tool for analyzing time-to-event data. By adjusting the shape and scale parameters, it can adapt to different real-world scenarios, making it suitable for a wide range of applications involving reliability, survival analysis, and extreme value modeling.