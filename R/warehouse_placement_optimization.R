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

warehouse.x <- 0
warehouse.y <- 0

# Functions & Formulas
places <- data.frame(
  number = c(1:5),
  object = c(LETTERS[seq(from = 1, to = 5)]),
  cargo_volume = c(25000, 30000, 70000, 25000, 10000),
  rate = c(45, 90, 90, 60, 80),
  coords.x = c(25, 10, 15, 16, 30),
  coords.y = c(60, 50, 70, 80, 100)
)

iterations <- data.frame(
  number = c(),
  coords.x = c(),
  coords.y = c(),
  tc = c()
)

get_init_warehouse_coords <- function(places) {
  x0 = sum(places$coords.x * places$cargo_volume * places$rate) / sum(places$cargo_volume * places$rate)
  y0 = sum(places$coords.y * places$cargo_volume * places$rate) / sum(places$cargo_volume * places$rate)
  return(c(x0, y0))
}

get_coords <- function() {
  
}

get_iteration_warehouse_coords <- function(places) {
  x0 <- sum((places$coords.x * places$cargo_volume * places$rate) / places$distance) / sum((places$cargo_volume * places$rate) / places$distance)
  y0 <- sum((places$coords.y * places$cargo_volume * places$rate) / places$distance) / sum((places$cargo_volume * places$rate) / places$distance)

  return(c(x0, y0))
}

distance_between_two_points <- function(xi, yi, x0, y0) sqrt((xi - x0) ^ 2 + (yi - y0) ^ 2)
get_total_cost <- function(cargo_volume, rate, distance) sum(cargo_volume * rate * distance)

# Programm Start
warehouse <- get_init_warehouse_coords(places)
warehouse.x <- warehouse[1]
warehouse.y <- warehouse[2]
places$distance <- distance_between_two_points(places$coords.x, places$coords.y, warehouse.x, warehouse.y)
total_cost <- get_total_cost(places$cargo_volume, places$rate, places$distance)
iterations <- rbind(iterations, data.frame(number = 1, coords.x = warehouse.x, coords.y = warehouse.y, tc = total_cost))

for (i in 2:10) {
  warehouse <- get_iteration_warehouse_coords(places)
  warehouse.x <- warehouse[1]
  warehouse.y <- warehouse[2]
  places$distance <- distance_between_two_points(places$coords.x, places$coords.y, warehouse.x, warehouse.y)
  total_cost <- get_total_cost(places$cargo_volume, places$rate, places$distance)
  iterations <- rbind(iterations, data.frame(number = i, coords.x = warehouse.x, coords.y = warehouse.y, tc = total_cost))
}

places$distance <- round(places$distance, 2)

par(xpd = FALSE, bg = color.bg)
plot(x = places$coords.x, y = places$coords.y,
  pch = 19,
  cex = 1.5,
  col = color.green,
  xlab = "X",
  ylab = "Y",
  col.lab = color.fg
)
points(warehouse.x, warehouse.y, col = color.red, pch = 19)
grid(col = color.fg, lty = 'dotted')
box(col = color.purple)
axis(1, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
axis(2, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
title('Warehouse Map', col.main = color.fg)



# par(xpd = FALSE, bg = color.bg)
# plot(x = iterations$number, y = iterations$tc,
#     type = 'o',
#     pch = 19,
#     col = color.green,
#     xlab = "X",
#     ylab = "Y",
#     col.lab = color.fg
# )
# box(col = color.purple)
# axis(1, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
# axis(2, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
# title('Iterations', col.main = color.fg)

