library(readxl)
office<- read_excel("D:/jayashrinidhi/office.xlsx")
print(office)

b.
#outliers
install.packages("outliers")
library(outliers)
test <- grubbs.test(office$salary)

c
#histogram
x <-office$salary
hist(x)

#barchart
barplot(x)

#piechart
pie(x)

a
#boxplot
boxplot(x)

#scatterplot
install.packages("scatterplot3d")
library(scatterplot3d)
attach(office)
scatterplot3d(`Total (50)`,`ETE (50)`,`MTE (25)`,main="3D scatterpolt")

attach(office)
plot(salary,id,main = "scatter_plot",xlab = "SALARY",ylab = "ID",pch=10)

