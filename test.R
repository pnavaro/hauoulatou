library(ggplot2)
library(dplyr)

titanic <- read.csv("titanic_full.csv")
count(titanic, Sex)
filter(titanic, Sex == "female")
arrange(titanic, Age)

ggplot(data = titanic) + aes(x = Age) + geom_histogram()
ggplot(data = titanic) + aes(x = Sex, y = Age) + geom_boxplot()

