### Computer lab 2 ###

### read the data set ###
GOOG <- read.csv("GOOG.csv")

### notice that we want a monthly data 
### But September has two observations, so I will remove the last row ###
GOOG <- GOOG[-61, ]

head(GOOG)
tail(GOOG)

### I do not want to keep the column high and low ###
### so I will remove comumn #3 and #4 ###
GOOG <- GOOG[ , -c(3, 4)]

### Next step is to calculate the log returns ###
GOOG$logclose <- log(GOOG$Close)

###log(A/B) =  log(A) - log(B)

GOOG$logreturn <- c(0, diff(GOOG$logclose))
### note: if you do not add 0 or NA in the frist row, you will
### get an error saying that you try to add a column with less rows than
### the already existed ###

### in order to have returns for all the observations ###
GOOG <- GOOG[-1, ]

### so our new start month is November 2016 ###
### I make use of the "ts" function that creates a time-series objects

GOOG$Close <-ts(GOOG$Close, start =c(2016, 11), frequency = 12)
GOOG$logreturn <-ts(GOOG$logreturn, start =c(2016, 11), frequency = 12)

ts.plot(GOOG$Close, main = "close vs time", ylab = "close")

ts.plot(GOOG$logreturn, main = "log return vs time", ylab = "log return")
abline(h = 0, lty = 2, col = "dark red")



### The last 4 observations will be the testing set ###
testing <- GOOG[(nrow(GOOG) - 3):nrow(GOOG), ]

###the first 55 are the training set ###
training <- GOOG[1: (nrow(GOOG) - 4), ]

### library that I need ###
### install.packages("forecast")

library(forecast)
holt_model <- holt(training$Close, h = 4, exponential = FALSE)
summary(holt_model)

plot(holt_model)
lines((nrow(GOOG) - 3):nrow(GOOG), testing$Close, col = "dark red",
      lty = 2, lwd = 2, type = "o")


plot(holt_model, xlim = c(50, nrow(GOOG)))
lines((nrow(GOOG) - 3):nrow(GOOG), testing$Close, col = "dark red", 
      lty = 2, lwd = 2, type = "o")

holt_forecast <- holt_model$mean
testing_values <- testing$Close
holt_forecast_error <- testing_values - holt_forecast
holt_table <- data.frame(cbind(testing_values, holt_forecast,
                               holt_forecast_error))
holt_table

### in order to raise in square to write ^2
### in order to sum you use the function sum 
### in order to take the square root you use the function sqrt()
### try to calculate RMSE

### I will use the library
### install.packages("tseries")
library(tseries)
adf.test(GOOG$Close)

adf.test(GOOG$Close, k = 1)

