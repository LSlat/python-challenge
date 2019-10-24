# Dependencies
import os
import csv

# File path
csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
net_change_list = []
greatest_increase = []
greatest_decrease = []

tot_months = 0
tot_net = 0
greatest_increase = 0
greatest_decrease = 999999999
month_increase = []
month_decrease = []
prev_net = 0

# Read the data in the file
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Header row
    csv_header = next(csvreader)

    # Get the first row of data
    first_row = next(csvreader)
    tot_months = tot_months + 1
    tot_net = tot_net + int(first_row[1])
    prev_net = prev_net + int(first_row[1])

    # Loop through data
    for row in csvreader:

        # Totals
        tot_months = tot_months + 1
        tot_net = tot_net + int(row[1])

        # Net amounts        
        net_change = int(row[1]) - int(prev_net)

        # Reset prev_net as loop through data
        prev_net = int(row[1])

        # Add the current net change to the list to calculate average
        net_change_list = net_change_list + [net_change]
        avg_net = round(sum(net_change_list) / len(net_change_list))

        # Greatest increase in profits
        if net_change > greatest_increase:
            month_increase = row[0]
            greatest_increase = net_change

        # Greatest decrease in losses
        if net_change < greatest_decrease:
            month_decrease = row[0]
            greatest_decrease = net_change

        # Average net change
        #avg_net = round(sum(net_change_list) / len(net_change_list))
        
# Print results
print(f"Financial Analysis")
print("------------------------------")
print(f"Total Months: {tot_months}")
print(f"Net Total: ${tot_net}")
print(f"Average Change: ${avg_net}")
print(f"Greatest Increase in Profits: {month_increase}, ${greatest_increase}")
print(f"Greatest Decrease in Losses: {month_decrease}, ${greatest_decrease}")

# File to output
output_file = os.path.join("Results.txt")

# Write to text file
with open("Results.txt", "w") as text_file:
    text_file.write(f"Financial Analysis\n")
    text_file.write("------------------------------\n")
    text_file.write(f"Total Months: {tot_months}\n")
    text_file.write(f"Net Total: ${tot_net}\n")
    text_file.write(f"Average Change: ${avg_net}\n")
    text_file.write(f"Greatest Increase in Profits: ${greatest_increase}\n")
    text_file.write(f"Greatest Decrease in Profits: ${greatest_decrease}\n")
    
   

    