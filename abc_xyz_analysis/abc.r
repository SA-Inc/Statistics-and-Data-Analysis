# Set work Directory.
print(getwd())
setwd("Desktop")

product_set <- read.csv("product_dataset_abc.csv")
product_income_sum <- sum(product_set$income)
product_set <- product_set[order(-product_set$income),]
product_set$percent <- round((product_set$income / product_income_sum) * 100, 2)
product_set$cumulative_percent <- cumsum(product_set$percent)
product_set$categories <- ifelse(product_set$cumulative_percent <= 80, "A", ifelse(product_set$cumulative_percent > 80 & product_set$cumulative_percent <= 95, "B", "C"))
write.csv(product_set, "product_abc_result.csv", row.names = FALSE)