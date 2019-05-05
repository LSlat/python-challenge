import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Lists to store data
tot_change = []
#net_change = []
greatest_change = []
least_change = []

#net_change = 0
tot_change = 0

greatest_change = 0
least_change = 0

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #---This 2nd NEXT throws results off(?)
    #firstrow = next(csvreader)
    #firstvalue = int(firstrow[1])
    #print(f"Header: {csv_header}")

    #new_header = ("Financial Analysis")
    #print(new_header)
    #print("--------------------------")

    #month_label = ("Total Months: ")
    #avg_label = ("Average Change: ")
    #max_inc_label = ("Greatest Increase in Profits: ")
    #min_inc_label = ("Greatest Decrease in Profits: ")

    for row in csvreader:
        net_change = int(row[2])
        previous = int(row[1])
        
        #prev_change = int(row[2])
        #if net_change > greatest_change:
         #   greatest_change = net_change
#print(greatest_change)
        
        
        
        #difference = int(row[1]) - firstvalue

        #---All of these dates print with each difference
        #Dates.append(row[0])
        #Profit_Loss.append(row[1])
        #difference.append(row[2])
        

        #tot_months = len(Dates)+1
        #net = net + int(row[1])

        #net = Profit_Loss.sum()
        #net = sum(Profit_Loss)
        #firstvalue = int(row[1])
        #print(firstvalue)
        #print(Dates)
        #print(difference)

        #total_diff = diff + int(row[1])

        

#---Gives wrong result     
avg_diff = total_diff/months

#---Gives error-'int' object is not iterable
#max_diff = max(difference)
#min_diff = min(difference)
print(f"Financial Analysis")
print("------------------------------")
print(f"Total Months: {months}")
print(f"Net Total: ")
print(f"Average Change: $")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")


#print(month_label + str(months))
#print(avg_label + str(avg_diff))

#print(max_diff)
#print(min_inc_label)       
#print(min_diff)
#print(f"Total Months: ", months)



# new_csv = zip(Dates, Profit_Loss)
#new_csv = (months)

# output_file = os.path.join("new_data.csv")
output_file = os.path.join("Results.txt")

with open("Results.txt", "w") as text_file:
    text_file.write(f"Financial Analysis\n")
    text_file.write("------------------------------\n")
    text_file.write(f"Total Months: {months}\n")
    text_file.write(f"Net Total: \n")
    text_file.write(f"Average Change: $\n")
    text_file.write(f"Greatest Increase in Profits: \n")
    text_file.write(f"Greatest Decrease in Profits: \n")
    
    #writer = csv.writer


    # writer.writerow(["Date", "Profit/Losses"])
    #writer.writerow([new_header])
    #writer.writerow(["----------------------------"])
    #text_file.write(new_header)
    

    #---from https://stackoverflow.com/questions/5214578/python-print-string-to-text-file
    #with open("Output.txt", "w") as text_file:
    #text_file.write("Purchase Amount: %s" % TotalAmount)

    #writer.writerow("Total Months: " )
    #writer.writerow(f[Total Months: ] + str(months))
    #writer.writerow(month_label, months)
    #writer.writerow(month_label + str(months))
    #text_file.write(month_label + str(months))

#for row in new_csv:
    #print(row)


    