# Cyberpunk Colorplate
color.bg = '#312A54'
color.fg = '#E6E5E6'
color.cursor = '#E84A62'
color.black = '#000000'
color.red = '#EE7993'
color.green = '#73F7B2'
color.yellow = '#FFFA81'
color.blue = '#55BCF9'
color.purple = '#D498F9'
color.cyan = '#95C9F9'
color.white = '#FFFFFF'

color_gradient <- colorRampPalette(c(color.blue, color.red))

# Linear Regression
products <- data.frame(
  month = c(1:12),
  costs = c(10, 12, 11, 12, 13, 14, 13, 15, 16, 14, 12, 10)
)

predicted_month <- 13

relation <- lm(costs ~ month, data = products)

result <- predict(relation, data.frame(month = predicted_month))

products <- rbind(products, data.frame(month = predicted_month, costs = NA))

par(xpd = F, bg = color.bg)
plot(x = products$month,
     y = products$costs,
     type = 'o',
     pch = 19,
     cex = 2,
     lwd = 2,
     xlab = "Month",
     ylab = "Sales",
     col = color.blue,
     col.lab = color.fg,
     )
title('Sales Forecasting(Linear Regression)', col.main = color.fg)
box(col = color.purple)
axis(side = 1, col = color.purple, col.ticks = color.purple, col.axis = color.cyan, at = products$month)
axis(side = 2, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
abline(relation, col = color.green, lwd = 2)
last_month <- products[nrow(products) - 1, ]
segments(last_month$month, last_month$costs, predicted_month, result, col = c(color.red), lwd = 2)
points(x = predicted_month, y = result, col = color.red, pch = 16, cex = 2)

# Multiple Regression
# input <- mtcars[, c("mpg","disp","hp","wt")]
# model <- lm(mpg ~ disp + hp + wt, data = input)
# 
# a <- coef(model)[1]
# Xdisp <- coef(model)[2]
# Xhp <- coef(model)[3]
# Xwt <- coef(model)[4]
# 
# get_mpg <- function(a, disp, hp, wt) a + Xdisp * disp + Xhp * hp + Xwt * wt
# 
# layout(matrix(c(1,2,3,4), 2, 2))
# plot(model)
