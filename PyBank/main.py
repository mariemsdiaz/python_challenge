import os

#Import csv reading module 
import csv

#Set a Path between operating system and csv file
csvpath="Resources/budget_data.csv"

#Set the output path for the text file creation 
output_path="analysis/text_analisys.txt"

#Initialize Variables for the values we want to find in csv file
total_months=0
greatest_increase=["",0]
greatest_decrease=["",10000000]
net_total=0
profit_loss_changes=[]
profit_loss_average=0
dates=[]

#Open the CSV File 
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#Skip the first header row
    next(csvreader)

#Add values to first row, previous row, and total months
    first_row= next(csvreader)
    profit_loss_previous=int(first_row[1])
    total_months += 1

#Figure out the net total value of all the months 
    net_total+= int(first_row[1])

#Start a Loop through all the Rows that counts the total number of months
    for row in csvreader:
        total_months += 1

#Now calculate the net total
        net_total+= int(row[1])

#Calculate the profit/loss change
        profit_loss_start=int(row[1])
        if total_months>1:
            changes= profit_loss_start-profit_loss_previous
            profit_loss_changes.append(changes)
            dates.append(row[0])
            profit_loss_previous=profit_loss_start
          
            
#Start checking for the greatest increase and greatest decrease.
greatest_increase=max(profit_loss_changes)
greatest_decrease=min(profit_loss_changes)
increase_date=dates[profit_loss_changes.index(greatest_increase)]
decrease_date=dates[profit_loss_changes.index(greatest_decrease)]


#Calculate what the average change is for the all the values in Profit/Losses. Changes divided by the number of items(len)=average

profit_loss_average=sum(profit_loss_changes)/len(profit_loss_changes)

#Print Results as an Analysis Summary. Hint to remember formatting to include only 2 decimal places for average with "":.2f"

print("Financial Analysis")
print("------------------------------")
print(f"Total Months:{total_months}")
print(f"Total:${net_total}")
print(f"Average Change: ${profit_loss_average:.2f}")
print(f"Greatest Increase in Profits: {increase_date} {greatest_increase}")
print(f"Greatest Decrease in Profits: {decrease_date} {greatest_decrease}")


#Create the text that will be included in the file as "output"
output=(
f"Financial Analysis\n"
f"------------------------------\n"
f"Total Months:{total_months}\n"
f"Total:${net_total}"
f"Average Change: ${profit_loss_average:.2f}\n"
f"Greatest Increase in Profits: {increase_date} {greatest_increase}\n"
f"Greatest Decrease in Profits: {decrease_date} {greatest_decrease}\n"
)

#Export the results into a text file 
with open(output_path,"w") as textfile:
    textfile.write(output)

