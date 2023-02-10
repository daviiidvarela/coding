data = read.csv("KO.csv")
plot(x = 1:731,y = data$Close,
     xlab = "Weeks since Jan 1, 2009",
     ylab = "Closing Price ($USD)",
     main = "The Coca-Cola Company (KO) closing price",
     pch = 19,
     cex = 0.5
)
