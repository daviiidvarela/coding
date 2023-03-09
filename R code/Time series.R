##install.packages("forecast")
##install.packages("tseries")
##install.packages("lmtest")


library(forecast)
library(tseries)
library(lmtest)





BLK

BLK <- BLK[,-c(3,4)]

BLK$logclose <-log(BLK$Close)

BLK$logreturn <-c(NA,diff(BLK$logclose))

BLK$log_Adj.close <-log(BLK$Adj.Close)

BLK$logreturn_Adj.close <-c(NA, diff(BLK$log_Adj.close))





BLK$Close <-ts(BLK$Close, start =c(2017, 01), frequency = 12)
BLK$logreturn <-ts(BLK$logreturn, start =c(2017, 01), frequency = 12)
ts.plot(BLK$Close ,  main = "close vs time" ,  ylab = "close" )

ts.plot(BLK$logreturn ,  main = "log return vs time" ,  ylab = "log return" )
abline(h = 0, lty = 2 , col = "dark red" )

training <- BLK[1:(nrow(BLK)-4), ]

testing <- BLK[(nrow(BLK)-3):nrow(BLK), ]

holt_model <-holt(training$Close, h = 4, exponential = FALSE)

summary(holt_model)

plot(holt_model)

lines((nrow(BLK)-3):nrow(BLK), testing$Close,col = "dark red", lty = 1, lwd = 2, type = "o")

adf.test(BLK$logreturn_Adj.close[-1], k =1)