import pathlib
import csv

# Point to the data file
csvpath = pathlib.Path("Resources/election_data.csv")

# Create empty variables to count candidate votes
Khan_Count = 0
Correy_Count = 0
Li_Count = 0
O_Tooley_Count = 0

with open(file=csvpath, mode='r') as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
     
# Read the header row first to skip it, since we don't want to include it in our column lists
    csv_header = next(csvreader)

# Subtotal votes for each candidate
    for row in csvreader:
       if row[2] == "Khan":
           Khan_Count = Khan_Count + 1
       elif row[2] == "Correy":
           Correy_Count = Correy_Count + 1
       elif row[2] == "Li":
           Li_Count = Li_Count + 1
       else:
           O_Tooley_Count = O_Tooley_Count + 1 

# Compute overall total votes
Total = Khan_Count + Correy_Count + Li_Count + O_Tooley_Count

# Compute percentages for each candidate
Khan_Percent = Khan_Count/Total*100
Correy_Percent = Correy_Count/Total*100
Li_Percent = Li_Count/Total*100
O_Tooley_Percent = O_Tooley_Count/Total*100

# Create a list of the candidates
TotalList = [Khan_Count,Correy_Count,Li_Count,O_Tooley_Count]

# Determine the winner based upon the total number of votes
if TotalList.index(max(TotalList)) == 0:
    Winner = "Khan"
elif TotalList.index(max(TotalList)) == 1:
    Winner = "Correy"
elif TotalList.index(max(TotalList)) == 2:
    Winner = "Li"
else: 
    Winner = "O'Tooley"

# Print our results to the terminal
print(f"Election Results")
print("-----------------")
print(f"Total Votes: {Total}")
print("-----------------")
print(f"Khan: {Khan_Percent:.3f}% ({Khan_Count})")
print(f"Correy: {Correy_Percent:.3f}% ({Correy_Count})")
print(f"Li: {Li_Percent:.3f}% ({Li_Count})")
print(f"O'Tooley: {O_Tooley_Percent:.3f}% ({O_Tooley_Count})")
print("-----------------")
print(f"Winner: {Winner}")
print("-----------------")


# Specify the file to write to
output_path = pathlib.Path("analysis/PyPoll_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file=output_path, mode='w') as csvfile:

# Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

# Write the table with the results
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['Total Votes',Total])
    csvwriter.writerow(['Candidate', 'Percentage','Votes'])
    csvwriter.writerow(['Khan',Khan_Percent/100,Khan_Count])
    csvwriter.writerow(['Correy',Correy_Percent/100,Correy_Count])
    csvwriter.writerow(['Li',Li_Percent/100,Li_Count])
    csvwriter.writerow(["O'Tooley",O_Tooley_Percent/100,O_Tooley_Count])
    csvwriter.writerow(["Winner",Winner])
