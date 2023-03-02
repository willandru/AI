head(diamonds)
model <- lm(diamonds$price~ diamonds$carat)
summary(model)
