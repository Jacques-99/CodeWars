library(tidyverse)

two_oldest_ages <- function(ages){
  ages <- sort.int(ages,decreasing = FALSE)
  ages <- ages[c(length(ages)-1,length(ages))]
  return(ages)
}

a <- c(1,2,8,10,1,5,87,45,8,8)
two_oldest_ages(a)

#Best answer:-------------
two_oldest_ages <- function(ages){
  tail(sort(ages), 2)
}

#input --> output
#[1, 2, 10, 8] --> [8, 10]
#[1, 5, 87, 45, 8, 8] --> [45, 87]
#[1, 3, 10, 0]) --> [3, 10]