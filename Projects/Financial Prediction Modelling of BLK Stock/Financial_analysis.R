##install.packages("forecast")
##install.packages("tseries")
##install.packages("lmtest")
##install.packages("Metrics")
##install.packages("FinTS")



library(forecast)
library(tseries)
library(lmtest)
library(Metrics)




BLK

BLK <- BLK[,-c(3,4)]

BLK$logclose <-log(BLK$Close)

BLK$logreturn <-c(NA,diff(BLK$logclose))

BLK$log_Adj.close <-log(BLK$Adj.Close)

BLK$logreturn_Adj.close <-c(NA, diff(BLK$log_Adj.close))

BLK$time <- 1:nrow(BLK)



BLK$Close <-ts(BLK$Close, start =c(2017, 01), frequency = 12)
BLK$logreturn <-ts(BLK$logreturn, start =c(2017, 01), frequency = 12)
ts.plot(BLK$Close ,  main = "close vs time" ,  ylab = "close" )

ts.plot(BLK$logreturn ,  main = "log return vs time" ,  ylab = "log return" )
abline(h = 0, lty = 2 , col = "dark red" )

training <- BLK[1:(nrow(BLK)-4), ]

testing <- BLK[(nrow(BLK)-3):nrow(BLK), ]


adf.test(BLK$logreturn_Adj.close[-1], k =1)


ARIMA010 <- Arima(training$log_Adj.close, order = c(0, 1, 0), include.drift =T)
summary(ARIMA010)

confint(ARIMA010)

coeftest(ARIMA010)

checkresiduals(ARIMA010)

regression <- lm(formula = Adj.Close ~ time, data = training)
summary(regression)

forward_data <- data.frame(time = 69:72)
regression_forecast <- predict.lm(regression, newdata = forward_data)

plot((1:nrow(BLK)), BLK$Adj.Close, type = "l", xlim = c(0, 72))
lines((1:(nrow(BLK) - 4)), regression$fitted.values, col = "dark blue", lwd = 2, lty = 2)
lines(69:72, testing$Adj.Close, type =  "o", col = "dark red", lwd = 2)
lines(69:72, regression_forecast, type =  "o", col = "dark blue", lwd = 2)

regression_forecast_error <- testing$Adj.Close - regression_forecast
regression_table <- data.frame(cbind(testing$Adj.Close, regression_forecast, regression_forecast_error))
names(regression_table) <- c("testing", "estimated", "residuals")

RMSE_regression <- rmse(regression_table$testing,regression_table$estimated)
RMSE_regression

holt_model <-holt(training$Close, h = 4, exponential = FALSE)

summary(holt_model)

plot(holt_model)
lines((nrow(BLK)-3):nrow(BLK), testing$Close,col = "dark red", lty = 1, lwd = 2, type = "o")

holt_forecast <- holt_model$mean
holt_forecast_error <- testing$Adj.Close - holt_forecast

holt_table <-data.frame(cbind(testing$Adj.Close, holt_forecast, holt_forecast_error))
names(holt_table) <- c("testing", "Holt's forecast","Holt's forecast error")
holt_table

RMSE_HOlt<-rmse(holt_table$testing,holt_table$`Holt's forecast`)
RMSE_HOlt

Acf(training$logreturn_Adj.close, main = "ACF", lag.max=12)

Pacf(training$logreturn_Adj.close, main = "PACF",lag.max=12)

ARIMA414 <- Arima(training$log_Adj.close, order = c(4, 1, 4), include.drift =T)
summary(ARIMA414)
coeftest(ARIMA414)

ARIMA314 <- Arima(training$log_Adj.close, order = c(3, 1, 4), include.drift =T)
summary(ARIMA314)
coeftest(ARIMA314)

ARIMA313 <- Arima(training$log_Adj.close, order = c(3, 1, 3), include.drift =T)
summary(ARIMA313)
coeftest(ARIMA313)

ARIMA312 <- Arima(training$log_Adj.close, order = c(3, 1, 2), include.drift =T)
summary(ARIMA312)
coeftest(ARIMA312)

ARIMA212 <- Arima(training$log_Adj.close, order = c(2, 1, 2), include.drift =T)
summary(ARIMA212)
coeftest(ARIMA212)

ARIMA211 <- Arima(training$log_Adj.close, order = c(2, 1, 1), include.drift =T)
summary(ARIMA211)
coeftest(ARIMA211)

ARIMA111 <- Arima(training$log_Adj.close, order = c(1, 1, 1), include.drift =T)
summary(ARIMA111)
coeftest(ARIMA111)
checkresiduals(ARIMA111)

ARIMA110 <- Arima(training$log_Adj.close, order = c(1, 1, 0), include.drift =T)
summary(ARIMA110)
coeftest(ARIMA110)
checkresiduals(ARIMA110)


ARIMA011 <- Arima(training$log_Adj.close, order = c(0, 1, 1), include.drift =T)
summary(ARIMA011)
coeftest(ARIMA011)
checkresiduals(ARIMA011 )

AIC_table <- data.frame(cbind(ARIMA010$aic, ARIMA011$aic, ARIMA110$aic, ARIMA111$aic),row.names = "AIC")
names(AIC_table) <- c("ARIMA(0, 1, 0)", "ARIMA(0, 1, 1)", "ARIMA(1, 1, 0)","ARIMA(1, 1, 1)")
AIC_table

BIC_table <- data.frame(cbind(ARIMA010$bic, ARIMA011$bic, ARIMA110$bic, ARIMA111$bic),row.names = "BIC")
names(BIC_table) <- c("ARIMA(0, 1, 0)", "ARIMA(0, 1, 1)", "ARIMA(1, 1, 0)","ARIMA(1, 1, 1)")
BIC_table

log2price <-function(a.forecast){
  a.forecast$mean <- exp(a.forecast$mean)
  a.forecast$upper <- exp(a.forecast$upper)
  a.forecast$lower <- exp(a.forecast$lower)
  a.forecast$x <- exp(a.forecast$x)
  return(a.forecast)}

forecast010 <- forecast(ARIMA010, h = 4)
priceforecast010 <- log2price(forecast010)
plot(priceforecast010)
lines(69:72, testing$Adj.Close, type = "o", col = "dark red", lwd = 2)

ARIMA010_forecast <- exp(forecast010$mean)
ARIMA010_forecast_error <- testing$Adj.Close - ARIMA010_forecast
ARIMA010_table <- data.frame(cbind(testing$Adj.Close, ARIMA010_forecast, ARIMA010_forecast_error))
ARIMA010_table

RMSE_ARIMA010<-rmse(ARIMA010_table$testing.Adj.Close,ARIMA010_table$ARIMA010_forecast)
RMSE_ARIMA010

forecast110 <- forecast(ARIMA110, h = 4)
priceforecast110 <- log2price(forecast110)
plot(priceforecast110)
lines(69:72, testing$Adj.Close, type = "o", col = "dark red", lwd = 2)

ARIMA110_forecast <- exp(forecast110$mean)
ARIMA110_forecast_error <- testing$Adj.Close - ARIMA110_forecast
ARIMA110_table <- data.frame(cbind(testing$Adj.Close, ARIMA110_forecast, ARIMA110_forecast_error))
ARIMA110_table

RMSE_ARIMA110<-rmse(ARIMA110_table$testing.Adj.Close,ARIMA110_table$ARIMA110_forecast)
RMSE_ARIMA110


forecast111 <- forecast(ARIMA111, h = 4)
priceforecast111 <- log2price(forecast111)
plot(priceforecast111)
lines(69:72, testing$Adj.Close, type = "o", col = "dark red", lwd = 2)

ARIMA111_forecast <- exp(forecast111$mean)
ARIMA111_forecast_error <- testing$Adj.Close - ARIMA111_forecast
ARIMA111_table <- data.frame(cbind(testing$Adj.Close, ARIMA111_forecast, ARIMA111_forecast_error))
ARIMA111_table

RMSE_ARIMA111<-rmse(ARIMA111_table$testing.Adj.Close,ARIMA111_table$ARIMA111_forecast)
RMSE_ARIMA111


forecast011 <- forecast(ARIMA011, h = 4)
priceforecast011 <- log2price(forecast011)
plot(priceforecast011)
lines(69:72, testing$Adj.Close, type = "o", col = "dark red", lwd = 2)

ARIMA011_forecast <- exp(forecast011$mean)
ARIMA011_forecast_error <- testing$Adj.Close - ARIMA011_forecast
ARIMA011_table <- data.frame(cbind(testing$Adj.Close, ARIMA011_forecast, ARIMA011_forecast_error))
ARIMA011_table

RMSE_ARIMA011<-rmse(ARIMA011_table$testing.Adj.Close,ARIMA011_table$ARIMA011_forecast)
RMSE_ARIMA011

RMSE_table <- data.frame(cbind(RMSE_ARIMA010, RMSE_ARIMA011, RMSE_ARIMA110, RMSE_ARIMA111, RMSE_HOlt, RMSE_regression),row.names = "RMSE")
names(RMSE_table) <- c("ARIMA(0, 1, 0)", "ARIMA(0, 1, 1)", "ARIMA(1, 1, 0)","ARIMA(1, 1, 1)","holt_model", "Regression_model")
RMSE_table

FinTS::ArchTest(ARIMA010$residuals)

FinTS::ArchTest(ARIMA110$residuals)

FinTS::ArchTest(ARIMA111$residuals)

FinTS::ArchTest(ARIMA011$residuals)






