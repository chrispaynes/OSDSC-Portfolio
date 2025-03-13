WHO = read.csv("./R/datasets/WHO.csv")

hist(WHO$CellularSubscribers)

# boxplot separated by country region
boxplot(WHO$LifeExpectancy ~ WHO$Region)

# boxplot separated by country region, with custom labels
boxplot(WHO$LifeExpectancy ~ WHO$Region, xlab="", ylab="Life Expectancy", main="Life Expectancy of Countries by Region")

# a basic table of the data
table(WHO$Region)
            #    Africa              Americas Eastern Mediterranean
            #        46                    35                    22
            #    Europe       South-East Asia       Western Pacific
            #        53                    11                    27

# splits table using the 2nd (Region) argument and then applies the 3rd argument (mean) to the first argument
tapply(WHO$Over60, WHO$Region, mean)
            #   Africa              Americas Eastern Mediterranean
            #  5.220652             10.943714              5.620000
            #    Europe       South-East Asia       Western Pacific
            # 19.774906              8.769091             10.162963

# table without removed N/A values
tapply(WHO$LiteracyRate, WHO$Region, min)
               Africa              Americas Eastern Mediterranean
                   NA                    NA                    NA
               Europe       South-East Asia       Western Pacific
                   NA                    NA                    NA

# table with removed N/A values
tapply(WHO$LiteracyRate, WHO$Region, min, na.rm=TRUE)
            #    Africa              Americas Eastern Mediterranean
            #      31.1                  75.2                  63.9
            #    Europe       South-East Asia       Western Pacific
            #      95.2                  56.8                  60.6