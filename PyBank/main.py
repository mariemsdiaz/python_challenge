import os

#Import csv reading module 
import csv

#Set a Path between operating system and csv file
csvpath=("budget_data.csv")

#Initialize Variables for the values we want to find in csv file
total_months=0
greatest_increase=["",0]
greatest_decrease=["",10000000]
net_total=0
profit_loss_changes=[]
profit_loss_average=[]


#Open the CSV File 
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Skip the first header row
    next(csvreader)

#Start a Loop through all the Rows that counts the total number of months
    for row in csvreader:
        total_months+= 1

#Now calculate the net total
    net_total+= int(row[1])

#Calculate the profit/loss change
    profit_loss_start=int(row[1])
    profit_loss_previous=0
    if total_months>1:
        profit_loss_changes= profit_loss_start-profit_loss_previous
     
        profit_loss_changes.append(profit_loss_changes)

#Start checking for the greatest increase and greatest decrease.

    if profit_loss_changes>greatest_increase[1]:
            greatest_increase=[row[0],profit_loss_changes]

    if profit_loss_changes<greatest_decrease[1]:
            greatest_decrease=[row[0],profit_loss_changes]

#Calculate what the average change is for the all the values in Profit/Losses

    profit_loss_average=sum(profit_loss_changes)/(total_months-1)

#Print Results as an Analysis Summary 

print("Financial Analysis")
print("------------------------------")
print(f"Total Months:{total_months}")
print(f"Total:${net_total}")
print(f"Average Change: ${profit_loss_average}")
print(f"Greatest Increase in Profits{greatest_increase}")
print(f"Greatest Decrease in Profits{greatest_decrease}")




