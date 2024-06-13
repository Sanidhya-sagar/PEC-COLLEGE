
#------- Question 1 -------#

library(tesseract)
library(gtranslate)

image_path <- "F:/menu_card.png"
ocr_engine <- tesseract()

menu_card <- ocr(image_path, engine = ocr_engine)


translated_menu <- translate(text = menu_card, to = "en")
print(translated_menu)

#------- Question 2 -------#

data <- read.csv(file = "F:/vs code folder/sem 4/supermarket sales.csv")

# Check for missing values
missing_values <- colSums(is.na(data))
print(missing_values)

most_frequent <- names(sort(table(data$Product.line), decreasing = TRUE))[1]
data$Product.line[is.na(data$Product.line)] <- most_frequent
print(most_frequent)

# Outlier removal
numeric_columns <- sapply(data, is.numeric)
z_scores <- scale(data[numeric_columns])
outliers <- rowSums(abs(z_scores) > 3, na.rm = TRUE) > 0
data <- data[!outliers, ]

# MinMax scaling
normalize <- function(x) {
  return((x - min(x)) / (max(x) - min(x)))
}

data[numeric_columns] <- lapply(data[numeric_columns], normalize)

model <- lm(Total ~ gross.income, data = data)

coef(model)


#prediction on data 
predictions <- predict(model, newdata = data)

# Calculating model performance
rmse <- sqrt(mean((data$Total - predictions)^2))
print(paste("RMSE:", rmse))

#summary of model
summary(model)

# Data visualization using ggplot2
library(ggplot2)

# Histogram of Total sales
ggplot(data, aes(x = Total)) + geom_histogram() + labs(title="Histogram of Total sales")

# Scatter plot of Total sales vs Quantity
ggplot(data, aes(x = gross.income, y = Total)) + geom_point() + labs(title="Scatter plot of Total sales vs Quantity")

# Box plot of Total sales by Product line
ggplot(data, aes(x = gross.income, y = Product.line)) + geom_boxplot() + labs(title="Box plot of Product line by gross income")









