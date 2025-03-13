# get the current working directory
getwd()

# read the CSV file in
WHO = read.csv("./R/datasets/WHO.csv")

# get the structure of the CSV
str(WHO)
# 'data.frame':   194 obs. of  13 variables:
#  variable name                    description of data type
#                                   Factor variables are non-numerical data points or categories.
#                                   lists how many categories or levels are in the variable
#  $ Country                      : Factor w/ 194 levels "Afghanistan",..: 1 2 3 4 5 6 7 8 9 10 ...
#  $ Region                       : Factor w/ 6 levels "Africa","Americas",..: 3 4 1 4 1 2 2 4 6 4 ...
#  $ Population                   : int  29825 3162 38482 78 20821 89 41087 2969 23050 8464 ...
#  $ Under15                      : num  47.4 21.3 27.4 15.2 47.6 ...
#  $ Over60                       : num  3.82 14.93 7.17 22.86 3.84 ...
#  $ FertilityRate                : num  5.4 1.75 2.83 NA 6.1 2.12 2.2 1.74 1.89 1.44 ...
#  $ LifeExpectancy               : int  60 74 73 82 51 75 76 71 82 81 ...
#  $ ChildMortality               : num  98.5 16.7 20 3.2 163.5 ...
#  $ CellularSubscribers          : num  54.3 96.4 99 75.5 48.4 ...
#  $ LiteracyRate                 : num  NA NA NA NA 70.1 99 97.8 99.6 NA NA ...
#  $ GNI                          : num  1140 8820 8310 NA 5230 ...
#  $ PrimarySchoolEnrollmentMale  : num  NA NA 98.2 78.4 93.1 91.1 NA NA 96.9 NA ...
#  $ PrimarySchoolEnrollmentFemale: num  NA NA 96.4 79.4 78.2 84.5 NA NA 97.5 NA ...

# get numerical summary of variables
summary(WHO)
#                 Country                      Region     Population
#  Afghanistan        :  1   Africa               :46   Min.   :      1
#  Albania            :  1   Americas             :35   1st Qu.:   1696
#  Algeria            :  1   Eastern Mediterranean:22   Median :   7790
#  Andorra            :  1   Europe               :53   Mean   :  36360
#  Angola             :  1   South-East Asia      :11   3rd Qu.:  24535
#  Antigua and Barbuda:  1   Western Pacific      :27   Max.   :1390000
#  (Other)            :188
#     Under15          Over60      FertilityRate   LifeExpectancy
#  Min.   :13.12   Min.   : 0.81   Min.   :1.260   Min.   :47.00
#  1st Qu.:18.72   1st Qu.: 5.20   1st Qu.:1.835   1st Qu.:64.00
#  Median :28.65   Median : 8.53   Median :2.400   Median :72.50
#  Mean   :28.73   Mean   :11.16   Mean   :2.941   Mean   :70.01
#  3rd Qu.:37.75   3rd Qu.:16.69   3rd Qu.:3.905   3rd Qu.:76.00
#  Max.   :49.99   Max.   :31.92   Max.   :7.580   Max.   :83.00
#                                  NA's   :11
#  ChildMortality    CellularSubscribers  LiteracyRate        GNI
#  Min.   :  2.200   Min.   :  2.57      Min.   :31.10   Min.   :  340
#  1st Qu.:  8.425   1st Qu.: 63.57      1st Qu.:71.60   1st Qu.: 2335
#  Median : 18.600   Median : 97.75      Median :91.80   Median : 7870
#  Mean   : 36.149   Mean   : 93.64      Mean   :83.71   Mean   :13321
#  3rd Qu.: 55.975   3rd Qu.:120.81      3rd Qu.:97.85   3rd Qu.:17558
#  Max.   :181.600   Max.   :196.41      Max.   :99.80   Max.   :86440
#                    NA's   :10          NA's   :91      NA's   :32
#  PrimarySchoolEnrollmentMale PrimarySchoolEnrollmentFemale
#  Min.   : 37.20              Min.   : 32.50
#  1st Qu.: 87.70              1st Qu.: 87.30
#  Median : 94.70              Median : 95.10
#  Mean   : 90.85              Mean   : 89.63
#  3rd Qu.: 98.10              3rd Qu.: 97.90
#  Max.   :100.00              Max.   :100.00
#  NA's   :93                  NA's   :93

# create a subset of data for Europe Specific data
WHO_Europe = subset(WHO, Region == "Europe")

# write the Europe Data Frame to a CSV
write.csv(WHO_Europe, "./R/datasets/WHO_EUROPE.csv")

# remove dataset from memory after checking to see if it is still in memory
ls()
#  [1] "AllCountryData" "Country"        "CountryData"    "LifeExpectancy"
#  [5] "NewCountryData" "Population"     "SquareRoot2"    "SquareRoot3"
#  [9] "WHO"            "WHO_Europe"

rm(WHO_Europe)
ls()
[1] "AllCountryData" "Country"        "CountryData"    "LifeExpectancy"
[5] "NewCountryData" "Population"     "SquareRoot2"    "SquareRoot3"
[9] "WHO"