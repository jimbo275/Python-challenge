import pathlib
import csv

# Point to the data file
csvpath = pathlib.Path("Resources/budget_data.csv")

# Create some empty lists to store the title, date, and profit/loss
date = []
Pl = []

with open(file=csvpath, mode='r') as csvfile:
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first to skip it, since we don't want to include it in our column lists
    csv_header = next(csvreader)

# Add each row after the header to the date and Pl lists we created above
    for row in csvreader:
        date.append(row[0])
        Pl.append(float(row[1]))

    # Take first difference of the Profit list    
    Difference = [Pl[i + 1] - Pl[i] for i in range(len(Pl)-1)]

    # Perform calculations on the lists we created
    Total = round(sum(Pl))
    DateLength = len(date)
    Average_Change = round(sum(Difference)/len(Difference),2)
    Max_Difference = round(max(Difference)) 
    Max_Index = Difference.index(Max_Difference)  
    Max_IndexDate = date[Max_Index+1]
    Min_Difference = round(min(Difference))
    Min_Index = Difference.index(Min_Difference) 
    Min_IndexDate = date[Min_Index+1]

# Print our results to the terminal
print(f"Financial Analysis")
print("-----------------")
print(f"Total months: {DateLength}")
print(f"Total: ${Total}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Max_IndexDate} (${Max_Difference})")
print(f"Greatest Decrease in Profits: {Min_IndexDate} (${Min_Difference})")

# Specify the file to write to
output_path = pathlib.Path("analysis/Pybank_output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file=output_path, mode='w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total months', 'Total', 'Average Change', 'Greatest_Increase in Profits_Date', 'Greatest Increase in Profits', 'Greatest Decrease in Profits Date', 'Greatest Decrease in Profts'])
    
    # Fill in the data rows
    csvwriter.writerow([DateLength,Total,Average_Change,Max_IndexDate,Max_Difference,Min_IndexDate,Min_Difference])
  

