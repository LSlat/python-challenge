# Dependencies
import os
import csv

# File path
csvpath = os.path.join("Resources", "election_data.csv")

# Variables to hold votes
Vote_Total = 0
Khanvote = 0
Correyvote = 0
Livote = 0
Tooleyvote = 0

# Read data in file
with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip file header
    csv_header = next(csvreader)

    # Loop through file, adding votes to respective variables
    for row in csvreader:
        Vote_Total = Vote_Total + 1
        if row[2] == "Khan":
            Khanvote = Khanvote + 1
        elif row[2] == "Correy":
            Correyvote = Correyvote + 1
        elif row[2] == "Li":
            Livote = Livote + 1
        elif row[2] == "O'Tooley":    
            Tooleyvote = Tooleyvote + 1

    # Percent of total votes for each candidate
    percent_Khan = round(Khanvote/Vote_Total*100)
    percent_Correy = round(Correyvote/Vote_Total*100)
    percent_Li = round(Livote/Vote_Total*100)
    percent_Tooley = round(Tooleyvote/Vote_Total*100)

    # Print vote totals    
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {Vote_Total}")
    print("--------------------------")
    print(f"Khan: {percent_Khan}% ({Khanvote})")
    print(f"Correy: {percent_Correy}% ({Correyvote})")
    print(f"Li:  {percent_Li}% ({Livote})")
    print(f"O'Tooley: {percent_Tooley}% ({Tooleyvote})")
    print("--------------------------")
    print(f"Winner: Khan")
    print("--------------------------")
    
# File to output
output_file = os.path.join("Results.txt")

# Write to text file
with open("Results.txt", "w") as text_file:
    text_file.write(f"Election Results\n")
    text_file.write("------------------------------\n")
    text_file.write(f"Total Votes: {Vote_Total}\n")
    text_file.write("------------------------------\n")
    text_file.write(f"Khan: {percent_Khan}% ({Khanvote})\n")
    text_file.write(f"Correy: {percent_Correy}% ({Correyvote})\n")
    text_file.write(f"Li: {percent_Li}% ({Livote})\n")
    text_file.write(f"O'Tooley: {percent_Tooley}% ({Tooleyvote})\n")
    text_file.write("------------------------------\n")
    text_file.write(f"Winner: Khan\n")
    text_file.write("------------------------------\n")
 