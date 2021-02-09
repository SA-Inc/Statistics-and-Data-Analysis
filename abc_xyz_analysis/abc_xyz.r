print(getwd())
setwd("Desktop")

sd.p = function(x){sd(x) * sqrt((length(x) - 1) / length(x))}

product_set <- read.csv("product_dataset_xyz.csv")
product_income_sum <- sum(product_set$income)
product_set <- product_set[order(-product_set$income),]
product_set$percent <- round((product_set$income / product_income_sum) * 100, 2)
product_set$cumulative_percent <- cumsum(product_set$percent)

product_set$mean <- rowMeans(subset(product_set, select=c(q1:q4)))
qs <- subset(product_set, select=q1:q4)
product_set$coefficient_variation <- round(apply(qs, 1, sd.p) * 100 / product_set$mean, 2)

product_set$categories_abc <- ifelse(product_set$cumulative_percent <= 80, "A", ifelse(product_set$cumulative_percent > 80 & product_set$cumulative_percent <= 95, "B", "C"))
product_set$categories_xyz <- ifelse(product_set$coefficient_variation <= 10, "X", ifelse(product_set$coefficient_variation > 10 & product_set$coefficient_variation <= 25, "Y", "Z"))

products = subset(product_set, select=c(product, categories_abc, categories_xyz))

write.csv(product_set, "product_abc_xyz_result.csv", row.names = FALSE)