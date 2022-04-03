# OS module allows you to interface with the underlying operating system that Python is running on
# csv module provides various classes for reading and writing data to CSV files
# shutil module offers a number of high-level operations on files and collections of files
import os
import csv
import shutil

# Set the path for the CSV file in PyPollcsv
PyPollcsv = os.path.join(r"PyPoll\resources\election_data.csv")

# Create the variables to store data
count = 0
candidate_list = []
candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path from PyPollcsv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidate_list
        candidate_list.append(row[2])
        # Create a set from the candidate_list to get the unique candidate names
    for x in set(candidate_list):
        candidate.append(x)
        # v is the total number of votes per candidate
        v = candidate_list.count(x)
        vote_count.append(v)
        # tvc is the percent of total votes per candidate
        tvc = (v/count)*100
        vote_percent.append(tvc)
        
    winning_vote_count = max(vote_count)
    winner = candidate[vote_count.index(winning_vote_count)]
 
# Printing the results
print("-------------------------")
print("Election Results")   
print("-------------------------")
print(f"Total Votes:{count}")    
print("-------------------------")
for i in range(len(candidate)):
                print(f"{candidate[i]}: {round(vote_percent[i],3)}%  ({vote_count[i]})")            
print("-------------------------")
print(f"The winner is: {winner}")
print("-------------------------")

# Print to a text file: election_results.txt 
# round function allows for the control of how many decimal places are in the answer
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write(f"Total Votes: {count}""\n")
    text.write("---------------------------------------\n")
    for i in range(len(candidate)):
        text.write(f"{candidate[i]}: {round(vote_percent[i],3)}%  ({vote_count[i]})""\n")
    text.write("---------------------------------------\n")
    text.write(f"The winner is: {winner}""\n")
    text.write("---------------------------------------\n")

# Moves the txt file into the analysis folder 
shutil.move("election_results.txt", r"PyPoll\analysis\election_results.txt")