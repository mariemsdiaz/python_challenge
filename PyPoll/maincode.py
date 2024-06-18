import os

#Import the csv reading module for Python
import csv

#Establish path fos csv file
csvpath="Resources/election_data.csv"

#Establish the path for text file 

output_path="analysis/text_analysis.txt"

#Initialize variables we want to find values for 

total_votes=0
candidates=[]
votes_per_candidate={}
winner=[]
#Open the csv file

with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")

#skip the first header 
    next(csvreader)

#Start a loops through all votes and canditates

    for row in csvreader:
        #total_votes+=1 #count the total numbe of votes of ALL CANDIDATES by increments 
        #Get candidates name from list 
        politician=row[2] #first candidates name 
        total_votes+=1
#Create a dictionary within the parent [Candidates] for each candidate
 #Add candidates to a list if they are not already there with an 'if' conditional 
        if politician not in candidates:
            candidates.append(politician)
            votes_per_candidate[politician]= 0
        #Count the votes for each candidate
        #else:
        else:
            votes_per_candidate[politician]+=1

#Calculate the percentage of votes for each candidate
    votes_percentages={}
    
    for politician in candidates: 
        votes_percentages[politician]= (votes_per_candidate[politician]/total_votes) * 100 


#Calculate the winner

winner=max(votes_per_candidate, key=votes_per_candidate.get)

#Print out results 

print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for politician in candidates:
    print(f"{politician}: {votes_percentages[politician]:.3f}% ({votes_per_candidate[politician]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


#Create the content of the output file
output = (
    f"Election Results\n"
    f"----------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"----------------------------------\n"
    )
for politician in candidates:
    output += (
        f"{politician}: {votes_percentages[politician]:.3f}% ({votes_per_candidate[politician]})\n"
    )

output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
    )

#Export the results into a text file 
with open(output_path,"w") as textfile:
    textfile.write(output)