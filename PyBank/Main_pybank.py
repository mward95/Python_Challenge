# OS module allows you to interface with the underlying operating system that Python is running on
# csv module provides various classes for reading and writing data to CSV files
# shutil module offers a number of high-level operations on files and collections of files
import os
import csv
import shutil

# Create a pathway for the this code to read the data in budget_data.csv
PyBankcsv = os.path.join(r"PyBank\resources\budget_data.csv")

# Brackets are used to declare a list and it contents in the program
profit = []
monthly_changes = []
date = []

# The variables used
month = 0
net_total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the CSV using the set path from PyBankcsv
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # for loop
    for row in csvreader: 

      # Use month to month the number months in this dataset
      month = month + 1 

      # Will need it when collecting the greatest increase and decrease in profits
      # After executing the method append on the list the size of the list increases by one.
      date.append(row[0])

      # Append the profit information & calculate the total profit
      profit.append(row[1])
      net_total_profit += int(row[1])

      #Calculate the average change in profits from month to month. Then calulate the average change in profits
      final_profit = int(row[1])
      monthly_change_profits = final_profit - initial_profit

      #Store these monthly changes in a list
      monthly_changes.append(monthly_change_profits)
          
      total_change_profits = total_change_profits + monthly_change_profits
      initial_profit = final_profit

      # Calculate the average change in profits
      average_change_profits = (total_change_profits/month)
      average_change_profits = (monthly_change_profits/month)
      
      #Find the max and min change in profits and the dates these changes happened
      greatest_increase_profits = max(monthly_changes)
      greatest_decrease_profits = min(monthly_changes)

      increase_date = date[monthly_changes.index(greatest_increase_profits)]
      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
  

    #had a lot of issues removing the very first number in the monthly_change_profts section. So I sliced it out and everything worked 
    monthly_changes = monthly_changes[1::]
    average_change_profits=(sum(monthly_changes)/ len(monthly_changes))

    # printing solution in the terminal
    # /n for the text.write moves the line down the next row
    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print(f"Total Months: {month}")
    print(f"Total Profits: ${net_total_profit}")
    print(f"Average Change:${int(average_change_profits)}") 
    print(f"Greatest Increase in Profits: {increase_date},(${greatest_increase_profits})")
    print(f"Greatest Decrease in Profits: {decrease_date},(${greatest_decrease_profits})")
    print("----------------------------------------------------------")
    # printing everything into a .txt file
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write(f"    Total Months: {month}""\n")
    text.write(f"    Total Profits: ${net_total_profit}""\n")
    text.write(f"    Average Change: ${int(average_change_profits)}""\n") 
    text.write(f"    Greatest Increase in Profits: {increase_date},(${greatest_increase_profits})""\n")
    text.write(f"    Greatest Decrease in Profits: {decrease_date},(${greatest_decrease_profits})""\n")
    text.write("----------------------------------------------------------\n")

# Moves the txt file into the analysis folder
shutil.move("financial_analysis.txt", r"PyBank\analysis\financial_analysis.txt")
