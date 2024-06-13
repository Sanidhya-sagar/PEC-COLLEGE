
s <- 34
print(s)

input <- mtcars[, c("mpg", "cyl")]
print(head(input))

# Load the dataset
data(mtcars)

# Create the box plot
boxplot(disp ~ gear, data = mtcars,
        main = "Displacement by Gear",
        xlab = "Gear",
        ylab = "Displacement")
