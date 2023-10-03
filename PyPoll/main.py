#This file reads a file with votes for any number of candidates.
#This code expects there to be a csv file name election_data.csv with two columns.

import csv

resourceLink = 'C:/Users/Steve/python/Bootcamp_Homework/python-challenge/PyPoll/Resources/election_data.csv'
analysisLink = 'C:/Users/Steve/python/Bootcamp_Homework/python-challenge/PyPoll/analysis/PyPoll_results.txt'

ballotID = []
county = []
candidate = []

electionDict = {}

totalVotes = 0
numOfWinnerVotes = 0

winnerName = []

csvpath = resourceLink

#lists to store data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Store the header
    csv_header = next(csvreader)
  
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
            electionDict[candidateName] = 1

        #We don't need to keep storing each row
        ballotID.clear()
        county.clear()
        candidate.clear()

#results
#text clean up using ... https://stackoverflow.com/questions/3151146/replace-the-single-quote-character-from-a-string
print("Election Results\n")
print("-------------------------------\n")
print(f"Total Votes: {totalVotes}\n")
print("-------------------------------\n")

#print list of results and clean up text
for key in electionDict:
    #https://stackoverflow.com/questions/3151146/replace-the-single-quote-character-from-a-string
    print(f"{key}: {round((electionDict[key]/totalVotes) * 100,2)}% ({electionDict[key]}) \n".replace('[','').replace(']','').replace("'","").replace('"',''))

    #find the highest number of votes
    if (electionDict[key] > numOfWinnerVotes):
         numOfWinnerVotes = electionDict[key]

#print winner(s)
for y in electionDict:
     if electionDict[y] == numOfWinnerVotes:
          winnerName.append(y)
         
print("-------------------------------\n")

#find the winner(s) - check for tie. If there is a tie, all winners are printed
for winner in winnerName:
    print(f"Winner: {winnerName}\n".replace('[','').replace(']','').replace("'","").replace('"',''))

print("-------------------------------\n")

#https://www.pythontutorial.net/python-basics/python-write-text-file/
#Work around from relative folder directory - Relative directories randomly stop working, but it doesn't seem to be required.
with open(analysisLink,'w', encoding='utf-8') as csvfile_out:
    csvfile_out.write("Election Results\n")
    csvfile_out.write("-------------------------------\n")
    csvfile_out.write(f"Total Votes: {totalVotes}\n")
    csvfile_out.write("-------------------------------\n")

    for key in electionDict:
        csvfile_out.write(f"{key}: {round((electionDict[key]/totalVotes) * 100,2)}% ({electionDict[key]}) \n".replace('[','').replace(']','').replace("'","").replace('"',''))

    csvfile_out.write("-------------------------------\n")

    for winner in winnerName:
        csvfile_out.write(f"Winner: {winnerName}\n".replace('[','').replace(']','').replace("'","").replace('"',''))

    csvfile_out.write("-------------------------------\n")