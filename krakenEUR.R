data = read.csv("/Users/Micha/Documents/bitbot/bit.bot/krakenEUR.csv", header=FALSE)
colnames(data) <- c("date", "price", "amount")

str(data)
head(data, n=3)
tail(data, n=3)

price=data$price
date=data$date
amount=data$amount

plot(date,price,type="l")

newdata <- subset(data, date >= 1500242400 & date < 1500328800, select=c(date, price, amount))
write.table(newdata, "/Users/Micha/Documents/bitbot/bit.bot/krakenEUR_lastDay.csv", sep=";")
data_day = read.csv("/Users/Micha/Documents/bitbot/bit.bot/krakenEUR_lastDay.csv", header=TRUE, sep=";")

str(newdata)
price_day=data_day$price
date_day=data_day$date
amount_day=data_day$amount

plot(date,price_day,type="l")
mean(price_day)
min(price_day)
max(price_day)

hist(amount_day)

# 39955 rows => nicht jede Sekunde ein Trade
