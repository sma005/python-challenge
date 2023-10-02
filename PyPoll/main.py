#This file reads a file with votes for any number of candidates.
#This code expects there to be a csv file name election_data.csv with two columns.

import os
import csv

ballotID = []
county = []
candidate = []

electionDict = {}

totalVotes = 0
numOfWinnerVotes = 0

winnerName = []
#This relative path isn't working. main.py is located in the PyBank folder, so it should
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv') 

#This relative path isn't working. main.py is located in the PyBank folder, so it should
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv') 
resourceLink = 'C:/Users/Steve/python/Bootcamp_Homework/python-challenge/PyPoll/Resources'
analysisLink = 'C:/Users/Steve/python/Bootcamp_Homework/python-challenge/PyPoll/analysis'

#Workaround solution
csvpath = os.path.join(resourceLink +'/election_data.csv')

#lists to store data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header
    next(csvreader)
  
    #import data 
    for row in csvreader:

        #converation with Ian from BCS. Learned about append
        ballotID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        candidateName = str(candidate)

        totalVotes = totalVotes + 1

        #add votes for each candidate
        if (candidateName) in electionDict:
                votes = electionDict.get(candidateName)
                electionDict[candidateName] = votes + 1
        else:
            #https://www.mygreatlearning.com/blog/python-dictionary-append/
            # #:~:text=Appending%20an%20empty%20dictionary%20means,the%20dict%5Bkey%
            # 5D%20method.&text=How%20do%20you%20add%20value,key%20value%20to%20the%20dictionary.
            electionDict[candidateName] = 1

        #We don't need to keep storing each row
        ballotID.clear()
        county.clear()
        candidate.clear()

#results
print("Election Results\n")
print("-------------------------------\n")
print(f"Total Votes: {totalVotes}\n")
print("-------------------------------\n")

#print list of results and clean up text
for key in electionDict:
    #https://stackoverflow.com/questions/3151146/replace-the-single-quote-character-from-a-string
    print(f"{key}: {round((electionDict[key]/totalVotes) * 100,2)}% ({electionDict[key]}) \n".replace('[','').replace(']','').replace("'",""))

    #find the highest number of votes
    if (electionDict[key] > numOfWinnerVotes):
         numOfWinnerVotes = electionDict[key]

#print winner(s)
for y in electionDict:
     if electionDict[y] == numOfWinnerVotes:
          winnerName.append(y)
         
print("-------------------------------\n")

#find the winner(s)
for winner in winnerName:
    print(f"Winner: {winnerName}\n".replace('[','').replace(']','').replace("'",""))

print("-------------------------------\n")

#https://www.pythontutorial.net/python-basics/python-write-text-file/
#Work around from relative folder directory - Relative directories randomly stop working, but it doesn't seem to be required.
with open(analysisLink + '/PyPoll_Results.txt', 'w', encoding='utf-8') as csvfile_out:
    csvfile_out.write("Election Results\n")
    csvfile_out.write("-------------------------------\n")
    csvfile_out.write(f"Total Votes: {totalVotes}\n")
    csvfile_out.write("-------------------------------\n")

    for key in electionDict:
    #https://stackoverflow.com/questions/3151146/replace-the-single-quote-character-from-a-string
        csvfile_out.write(f"{key}: {round((electionDict[key]/totalVotes) * 100,2)}% ({electionDict[key]}) \n".replace('[','').replace(']','').replace("'",""))

    csvfile_out.write("-------------------------------\n")

    for winner in winnerName:
        csvfile_out.write(f"Winner: {winnerName}\n".replace('[','').replace(']','').replace("'",""))

    csvfile_out.write("-------------------------------\n")
