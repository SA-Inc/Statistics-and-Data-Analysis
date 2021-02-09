getwd()
setwd('/Users/armansaparov/Desktop')

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

calc_storage_costs <- function(s) {
  warehouse_turnover <- 1.5 # оборот склада в месяц
  cargo_density <- 0.5 # плотность материального потока потока т/м3
  height <- 4 # высота укладки м
  warehouse_turnover_useful_area <- 0.4 # оборот склада от полезной площади склада
  warehouse_equipment_utilization <- 0.7 # коэфицент использования складского оборудования
  
  depreciation_period <- 20 # срок амортизации лет
  one_square_meter_storage <- 250 # стоимость 1м2 склада $
  transaction_costs <- 1.4 # операционные издержки $/тон
  annual_fixed_costs <- 40 # годовые постоянные затраты $/м2
  leasing <- 6.3 # стоимость аренды $ тон/мес
  cargo_hangling_costs <- 3.2 # стоимость услуг по переработки груза $/тон
  
  storage_costs <- data.frame(
    month = c(month.name),
    demand = c(427, 634, 993, 1407, 1766, 1973, 1973, 1766, 1407, 993, 634, 427)
  )
  
  storage_costs$area <- round(storage_costs$demand / (warehouse_turnover * cargo_density * height * warehouse_turnover_useful_area * warehouse_equipment_utilization))
  
  for (i in 1:length(storage_costs$area)) {
    if(storage_costs$area[i] < s) {
      storage_costs$cargo_distribution.own[i] = 100
      storage_costs$cargo_distribution.leased[i] = 0
    } else {
      storage_costs$cargo_distribution.own[i] = round(((s * 100) / storage_costs$area[i]), 2)
      storage_costs$cargo_distribution.leased[i] = 100 - round(((s * 100) / storage_costs$area[i]), 2)
    }
  }
  
  for (i in 1:length(storage_costs$area)) {
    storage_costs$general_costs.own[i] = s * (((one_square_meter_storage / depreciation_period) + annual_fixed_costs) / 12) + storage_costs$demand[i] * (storage_costs$cargo_distribution.own[i] / 100) * transaction_costs
    storage_costs$general_costs.leased[i] = storage_costs$demand[i] * (storage_costs$cargo_distribution.leased[i] / 100) * (leasing + cargo_hangling_costs)
    storage_costs$general_costs.total[i] = storage_costs$general_costs.own[i] + storage_costs$general_costs.leased[i]
  }
  
  return(c(sum(storage_costs$general_costs.own), sum(storage_costs$general_costs.leased), sum(storage_costs$general_costs.total)))
}

storage_costs_result <- data.frame(
  square = c(),
  own = c(),
  leased = c(),
  total = c()
)

for (i in seq(from = 0, to = 1200, by = 100)) {
  temp_result = calc_storage_costs(i)
  storage_costs_result <- rbind(storage_costs_result, data.frame(square = i, own = temp_result[1], leased = temp_result[2], total = temp_result[3]))
}

par(xpd = FALSE, bg = color.bg)
plot(storage_costs_result$square, storage_costs_result$total, type = 'o', col = color.red, pch = 19, ylim = c(0, max(storage_costs_result)), xlab = 'Warehouse Square (m^2)', ylab = 'Storage Costs ($ per Year)', col.lab = color.fg)
grid(col = color.fg, lty = 'dotted')
box(col = color.purple)
axis(1, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
axis(2, col = color.purple, col.ticks = color.purple, col.axis = color.cyan)
lines(storage_costs_result$square, storage_costs_result$leased, type = 'o', col = color.green, pch = 19)
lines(storage_costs_result$square, storage_costs_result$own, type = 'o', col = color.blue, pch = 19)
title('Dependence of the Costs of leased and own Warehouse Area', col.main = color.fg)
par(xpd = TRUE)
legend('left', inset = c(0), legend = c('Total','Leased', 'Own'), col = c(color.red, color.green, color.blue), title = 'Costs', pch = c(19), lty = c(1), text.col = c(color.fg), box.col = color.yellow, cex = 0.7)

print(storage_costs_result[which.min(storage_costs_result$total),])
