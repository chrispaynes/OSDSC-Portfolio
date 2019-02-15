# variable assignment
SquareRoot2 = sqrt(2)

# variable assignment
SquareRoot3 <- sqrt(3)

# lists objects that have been defined. formatted in a vector of strings
ls()

# read documentation 
# ?ls

# create vectors
Country <- c("brazil", "china", "india", "switzerland", "united states");
LifeExpectancy <- c(74,76,65,83,79)

# create a sequence of numbers
seq(0, 100, 2)
#  [1]   0   2   4   6   8  10  12  14  16  18  20  22  24  26  28  30  32  34  36
# [20]  38  40  42  44  46  48  50  52  54  56  58  60  62  64  66  68  70  72  74
# [39]  76  78  80  82  84  86  88  90  92  94  96  98 100

# access a sequence element by index. Indexed by 1 and not 0
Country[2] # "china"

CountryData <- data.frame(Country, LifeExpectancy)

CountryData
#         Country LifeExpectancy
# 1        brazil             74
# 2         china             76
# 3         india             65
# 4   switzerland             83
# 5 united states             79

# $ allows for adding a new property to the data frame
# vector values must be combined in the proper order to ensure they match up with existing data frame
CountryData$Population <- c(199000, 1390000, 1240000, 7997, 318000)

CountryData
#         Country LifeExpectancy Population
# 1        brazil             74     199000
# 2         china             76    1390000
# 3         india             65    1240000
# 4   switzerland             83       7997
# 5 united states             79     318000

# create another set of country data to later combine with the existing CountryData DF
Country <- c("australia", "greece")
LifeExpectancy <- c(82,81)
Population <- c(23050,11125)
NewCountryData = data.frame(Country, LifeExpectancy, Population)
NewCountryData
#     Country LifeExpectancy Population
# 1 australia             82      23050
# 2    greece             81      11125

# bind dataframes together
AllCountryData = rbind(CountryData, NewCountryData)
AllCountryData
#         Country LifeExpectancy Population
# 1        brazil             74     199000
# 2         china             76    1390000
# 3         india             65    1240000
# 4   switzerland             83       7997
# 5 united states             79     318000
# 6     australia             82      23050
# 7        greece             81      11125