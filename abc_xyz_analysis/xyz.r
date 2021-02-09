# Set work Directory.
print(getwd())
setwd("r")

sd.p = function(x){sd(x) * sqrt((length(x) - 1) / length(x))}

product_set <- read.csv("product_dataset_xyz.csv")
product_set$mean <- rowMeans(product_set[, 3:ncol(product_set)])
qs <- subset(product_set, select=q1:q4)
product_set$coefficient_variation <- round(apply(qs, 1, sd.p) * 100 / product_set$mean, 2)
product_set$category <- ifelse(product_set$coefficient_variation <= 10, "X", ifelse(product_set$coefficient_variation > 10 & product_set$coefficient_variation <= 25, "Y", "Z"))
write.csv(product_set, "product_xyz_result.csv", row.names = FALSE)
