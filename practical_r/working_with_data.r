WHO = read.csv("./R/datasets/WHO.csv")

# gets the "Under15" vector of the data frame
WHO$Under15
#   [1] 47.42 21.33 27.42 15.20 47.58 25.96 24.42 20.34 18.95 14.51 22.25 21.62
#  [13] 20.16 30.57 18.99 15.10 16.88 34.40 42.95 28.53 35.23 16.35 33.75 24.56
#  [25] 25.75 13.53 45.66 44.20 31.23 43.08 16.37 30.17 40.07 48.52 21.38 17.95
#  [37] 28.03 42.17 42.37 30.61 23.94 41.48 14.98 16.58 17.16 14.56 21.98 45.11
#  [49] 17.66 33.72 25.96 30.53 30.29 31.25 30.62 38.95 43.10 15.69 43.29 28.88
#  [61] 16.42 18.26 38.49 45.90 17.62 13.17 38.59 14.60 26.96 40.80 42.46 41.55
#  [73] 36.77 35.35 35.72 14.62 20.71 29.43 29.27 23.68 40.51 21.54 27.53 14.04
#  [85] 27.78 13.12 34.13 25.46 42.37 30.10 24.90 30.21 35.61 14.57 21.64 36.75
#  [97] 43.06 29.45 15.13 17.46 42.72 45.44 26.65 29.03 47.14 14.98 30.10 40.22
# [109] 20.17 29.02 35.81 18.26 27.05 19.01 27.85 45.38 25.28 36.59 30.10 35.58
# [121] 17.21 20.26 33.37 49.99 44.23 30.61 18.64 24.19 34.31 30.10 28.65 38.37
# [133] 32.78 29.18 34.53 14.91 14.92 13.28 15.25 16.52 15.05 15.45 43.56 25.96
# [145] 24.31 25.70 37.88 14.04 41.60 29.69 43.54 16.45 21.95 41.74 16.48 15.00
# [157] 14.16 40.37 47.35 29.53 42.28 15.20 25.15 41.48 27.83 38.05 16.71 14.79
# [169] 35.35 35.75 18.47 16.89 46.33 41.89 37.33 20.73 23.22 26.00 28.65 30.61
# [181] 48.54 14.18 14.41 17.54 44.85 19.63 22.05 28.90 37.37 28.84 22.87 40.72
# [193] 46.73 40.24

u15 <- WHO$Under15

mean(u15)

# Standard Deviation
sd(u15)

# summary of the vector
summary(u15)
#    Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
#   13.12   18.72   28.65   28.73   37.75   49.99

# find which country has the minimal amoun
# finds the row number with minimal observation of under 15
which.min(u15)
# [1] 86

# Japan has the smallest population of under 15 years olds
WHO$Country[86]
# [1] Japan
# 194 Levels: Afghanistan Albania Algeria Andorra Angola ... Zimbabwe

# find the max % of the population under15
WHO$Country[which.max(u15)]
# [1] Niger
# 194 Levels: Afghanistan Albania Algeria Andorra Angola ... Zimbabwe

# create a scatterplot of GNI compared to fertiility rate
plot(WHO$GNI, WHO$FertilityRate)

Outliers = subset(WHO, GNI > 10000 & FertilityRate > 2.5)

# find the number of rows
nrow(Outliers)

# output country names of outliers

Outliers[c("Country", "GNI", "FertilityRate")]
#               Country   GNI FertilityRate
# 23           Botswana 14550          2.71
# 56  Equatorial Guinea 25620          5.04
# 63              Gabon 13740          4.18
# 83             Israel 27110          2.92
# 88         Kazakhstan 11250          2.52
# 131            Panama 14510          2.52
# 150      Saudi Arabia 24700          2.76