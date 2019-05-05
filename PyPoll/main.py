import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

Vote_Total = 0
Kahnvote = 0
Correyvote = 0
Livote = 0
Tooleyvote = 0

with open(csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        Vote_Total = Vote_Total + 1
        if row[2] == "Kahn":
            Kahnvote = Kahnvote + 1
        elif row[2] == "Correy":
            Correyvote = Correyvote + 1
        elif row[2] == "Li":
            Livote == Livote + 1
        elif row[2] == "O'Tooley":    
            Tooleyvote = Tooleyvote + 1

#Why are the individual candidate (Khan and Li) vote totals wrong???

    percent_Kahn = Kahnvote/Vote_Total*100
    percent_Correy = Correyvote/Vote_Total*100
    percent_Li = Livote/Vote_Total*100
    percent_Tooley = Tooleyvote/Vote_Total*100
        
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {Vote_Total}")
    print("--------------------------")
    print(f"Khan: {percent_Kahn}% ({Kahnvote})")
    print(f"Correy: {percent_Correy}% ({Correyvote})")
    print(f"Li:  {percent_Li}% ({Livote})")
    print(f"O'Tooley: {percent_Tooley}% ({Tooleyvote})")
    print("--------------------------")
    print(f"Winner: Khan")
    print("--------------------------")
    
output_file = os.path.join("Results.txt")

with open("Results.txt", "w") as text_file:
    text_file.write(f"Election Results\n")
    text_file.write("------------------------------\n")
    text_file.write(f"Total Votes: {Vote_Total}\n")
    text_file.write(f"Kahn: {percent_Kahn}% ({Kahnvote})\n")
    text_file.write(f"Correy: {percent_Correy}% ({Correyvote})\n")
    text_file.write(f"Li: {percent_Li}% ({Livote})\n")
    text_file.write(f"O'Tooley: {percent_Tooley}% ({Tooleyvote})\n")
    text_file.write("------------------------------\n")
    text_file.write(f"Winner: Khan\n")
    text_file.write("------------------------------\n")
