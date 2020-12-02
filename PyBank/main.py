# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

#Import libraries
import os
import csv

#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")

total_months = 0
total_profitloss = 0
value = 0
change = 0
dates = []
profits = []

#Open and read CSV file
with open("Resources/budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading header row
    csv_header = next(csvreader)

    #Reading first row (to track changes)
    first_row = next(csvreader)
    total_months = total_months+1
    total_profitloss += int(first_row[1])
    value = int(first_row[1])
    
    #Going through each row of data after header & first row 
    for row in csvreader:
        # Keeping track of the dates
        dates.append(row[0])
        
        # Calculate the change then add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months = total_months+1

        #Total net amount of "Profit/Losses over entire period"
        total_profitloss = total_profitloss + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    
#Displaying information
OutputAnalysis=(
    f"Financial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profitloss}\n"
    f"Average Change: ${(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {worst_date} (${greatest_decrease})"
    )
print (OutputAnalysis)

# Exporting to .txt file
with open("Analysis/output.txt", "w") as output:
    output.write(OutputAnalysis)
