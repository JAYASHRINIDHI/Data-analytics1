#mean:
  mean(marks$Total)

#median:
  median(marks$Total)

#mode:
  install.packages("modeest")
library(modeest)
mlv(marks$Total,method = "mfv")

#percentile:
  d <- c(marks$Total)
print(d)
quantile(d,c(0.50))

d1 <- c(1,2,3,4,5)
q1 <- quantile(d1,c(0.25))
print(q1)
q2 <- quantile(d1,c(0.50))
print(q2)
q3 <- quantile(d1,c(0.75))
print(q3)



#max and min:
  data <- c(1,3,4,463,2,3,6,8,9,4,254,6,72)
min(data)
max(data)

#range:
  r <- range(data)
diff(r)

#variance:
  var(marks$Total)

#sd:
  sd(marks$Total)

  #interquartile
    IQ=q3-q1
   print(IQ)
  
  #population standard deviation
    n <-  length(marks$Total)
  sd(marks$Total)*sqrt((n-1)/n)

  
  #skew
  skewness(marks$Total)
 
  
  #Boxplot
     boxplot(marks$Total,horizontal = TRUE)
  
  