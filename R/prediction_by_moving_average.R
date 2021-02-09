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

get_moving_average <- function(x, n) filter(x, rep(1 / n, n))
get_average_relative_linear_change <- function(products) (abs(products$costs - products$prediction) / products$costs) * 100

products <- data.frame(
  month = c(1:12),
  costs = c(10, 12, 11, 12, 13, 14, 13, 15, 16, 14, 12, 10)
)

moving_average_step <- 3

products$prediction <- round(get_moving_average(products$costs, moving_average_step), 2)
products$average_relative <- round(get_average_relative_linear_change(products), 2)
relative_error <- (1 / length(na.omit(products$prediction))) * sum(products$average_relative, na.rm = T)
# length(products$month)
# length(na.omit(products$prediction))

par(xpd = T, mar = par()$mar + c(0,0,0,7), bg = color.bg)
plot(x = products$month,
     y = products$costs,
     type = 'o',
     pch = 19,
     xlab = "Month",
     ylab = "Sales",
     col = color.red,
     col.lab = color.fg,
     ylim=c(0, 20),
     bty='L'
     #panel.first=grid()
)

box(col = color.purple)
axis(1, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
axis(2, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
lines(x = products$month, y = products$prediction, type = 'o', col = color.green, pch = 19)
lines(x = products$month, y = products$average_relative, type = 'o', col = color.blue, pch = 19)
title('Sales Forecasting', col.main = color.fg)
legend(13, 20, legend = c('Current Sales', 'Predicted Sales', 'Average Relative'), col = c(color.red, color.green, color.blue), title = 'Costs', pch = c(19), lty = c(1), text.col = c(color.fg), box.col = color.yellow, cex = 0.8)
legend(13, 10, ncol = 1, legend = c('Relative Error', relative_error), text.col = c(color.fg), box.col = color.yellow, cex = 0.8)
par(xpd = F, mar=c(5, 4, 4, 2) + 0.1)
grid(col = color.fg, lty = 'dotted')
