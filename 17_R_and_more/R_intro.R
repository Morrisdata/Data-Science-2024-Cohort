# comments


#Get current working directory
getwd()

#Set Current working directory
setwd('C:/Users/Matth/OneDrive/Desktop/DATA')


#Loading the csv file and summary
# notice you do not have to import files and <- is the equivalent to python = 
bgg_org <- read.csv('bggdata.csv')

# get all the column names
colnames(bgg_org)


# get column names with specific data type
colnames(bgg_org[,sapply(bgg_org,is.numeric)])

# 
head(bgg_org)

tail(bgg_org)


# retrieve a single column
bgg_org$name


# use a function with a column
median(bgg_org$baverage)


subset(bgg_org, name == "War of the Ring")

# Bracket notation
# dataSet[ROWS, COLUMNS]

# returning all the columns
bgg_org[bgg_org$name == "War of the Ring",]


high_rate <- bgg_org[bgg_org$baverage >8,]
head(high_rate$name,2)


subset(bgg_org, baverage > 8 & average > 8)


#summary
colnames(bgg_org[,sapply(bgg_org,is.numeric)])

# Filter rows by column values
filter(bgg_org, 'avgweight' >= 4)
colnames(complex_games)


#Bracket notation
#dataSet[ROWS, COLUMNS]

#returning all the columns
complex_games<-bgg_org[bgg_org$avgweight >= 4,]

# unique values from a particular field
unique(complex_games[c("name")])

#summary
summary(complex_games)
summary(complex_games$avgweight)
summary(bgg_org$avgweight)



# isnull
!is.null(bgg_org)

colSums(is.na(bgg_org))


# duplicates
duplicated(bgg_org)
bgg_org[duplicated(bgg_org$name),]

bgg_org[!duplicated(bgg_org),]

# 
# if else
bgg_org$Result = ifelse(bgg_org$average >5,"highly rated games", "else low rated games") 
  print(bgg_org)

# basic plots

# Horizontal Bar Plot for  

barplot(complex_games$avgweight, 
        main = 'Review of complex games', 
        xlab = 'complexity level levels', col = 'light blue', horiz = FALSE) 


# histogram

hist(complex_games$avgweight, main ="Complexity of board games\ 
     minimum complexity of 4", 
     xlab ="complexity rating", 
     xlim = c(4, 5), col ="light blue", 
     freq = TRUE) 



# Box plot 

boxplot(complex_games$avgweight, main = "Complexity of board games\ 
     minimum complexity of 4", 
        xlab = "Complexity Rating", ylab = "frequency", 
        col = "orange", border = "brown", 
        horizontal = TRUE, notch = TRUE) 




boxplot(complex_games[, 16:17],  
        main ='score reviews') 


plot(complex_games$avgweight, complex_games$baverage, 
     main ="Scatterplot Example", 
     xlab ="complexity", 
     ylab =" review score", pch = 19) 

'''
Common R libraries
dplyr - data manipulation
tidyr - data wrangling and cleaning
ggplot2 - Grammar of Graphics
lubridate - helps with dates
Shiny - Very popular create and publish interactive dashboards. Worth getting into if you have time. 
tseries - Time Series
Prophet - forecasting tool
ggmap - maps maps maps
sqldf - combine r and sql
Caret - Classification and regression
'''
