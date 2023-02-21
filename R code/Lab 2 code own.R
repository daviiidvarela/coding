library(forecast)
library(tseries)

GOOG <-read.csv("/Users/davidvarela/Downloads/coding/R code/GOOG.csv")

tail(GOOG)

GOOG <- GOOG[-nrow(GOOG),]
GOOG <- GOOG[,-c(3,4)]

GOOG$logclose <-log(GOOG$Close)
GOOG$logreturn <-c(NA,diff(GOOG$logclose))
head(GOOG)

GOOG <- GOOG[-1, ]
GOOG$Close <-ts(GOOG$Close, start =c(2016, 11), frequency = 12)
GOOG$logreturn <-ts(GOOG$logreturn, start =c(2016, 11), frequency = 12)
ts.plot(GOOG$Close ,  main = "close vs time" ,  ylab = "close" )

ts.plot(GOOG$logreturn ,  main = "log return vs time" ,  ylab = "log return" )
abline(h = 0, lty = 2 , col = "dark red" ) #lty = 2 gives a dashed line

training <- GOOG[1:(nrow(GOOG)-4), ]
testing <- GOOG[(nrow(GOOG)-3):nrow(GOOG), ]

print(paste("The number of rows in my training set is",nrow(training)))
tail(training)

holt_model <-holt(training$Close, h = 4, exponential = FALSE)
### look at the parameters
summary(holt_model)

plot(holt_model)

lines((nrow(GOOG)-3):nrow(GOOG), testing$Close,
      col = "dark red", lty = 1, lwd = 2, type = "o")

plot(holt_model,
     xlim =c(50,nrow(GOOG)))
#Draw a red line where the testing data is
lines((nrow(GOOG)-3):nrow(GOOG), testing$Close,
      col = "dark red", lty = 1, lwd = 2, type = "o")

testing_values <- testing$Close
holt_forecast <- holt_model$mean ### for some reason these values are called "mean"
holt_forecast_error <- testing_values-holt_forecast
holt_table <-data.frame(cbind(testing_values, holt_forecast, holt_forecast_error))
holt_table

#Dickey Fuller test
adf.test(GOOG$Close)
adf.test(GOOG$Close, k = 1)

