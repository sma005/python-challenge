#This file reads profits and losses from a set time period, and calculates gains and losses

import os
import csv

month = []
profitLossGain = []
numOfMonths = 0
currentChange = 0 #the difference between the previous month and the current

biggestLoss = 0
biggestGain = 0

totalLossGain = 0
totalChange = 0

#Grab the data

#This relative path isn't working. main.py is located in the PyBank folder, so it should
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv') 

#Workaround solution
csvpath = os.path.join('C:/Users/Steve/python/Bootcamp_Homework/python-challenge/PyBank/Resources/budget_data.csv')

#lists to store data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header
    next(csvreader)

    #import data 
    for row in csvreader:
        month.append(row[0])
        profitLossGain.append(row[1])

        currentMonth = str(row[0])
        currentLossGain = int(row[1])

        numOfMonths +=1

        #Can't have profits/losses in the first month on this model
        if (numOfMonths != 1):
            currentChange = currentLossGain - previousLossGain

            if (currentChange < biggestLoss):
                biggestLoss = currentChange
                biggestLossMonth = currentMonth

            if (currentChange > biggestGain):
                biggestGain = currentChange
                biggestGainMonth = currentMonth

        #adjust the aggregates
        previousLossGain = currentLossGain
        previousMonth = currentMonth
        totalLossGain = totalLossGain + currentLossGain
        totalChange = totalChange + currentChange
       
print("Financial Analysis\n")
print("-----------------------------\n")
print(f"Total Months: {numOfMonths}\n")
print(f"Total: ${totalLossGain}\n")
print(f"Average Change: ${round(totalChange / (numOfMonths - 1), 2)} \n")
print(f"Greatest Increase in Profits: {biggestGainMonth} (${biggestGain})\n")
print(f"Greatest Decrease in Profits: {biggestLossMonth} (${biggestLoss})\n")

#https://www.pythontutorial.net/python-basics/python-write-text-file/
#Work around from relative folder directory
#with open('PyBank_Results.txt', 'w', encoding='utf-8') as csvfile_out:
with open('C:/Users/Steve/python/Bootcamp_Homework/python-challenge/PyBank/Resources/analysis.txt', 'w', encoding='utf-8') as csvfile_out:
    csvfile_out.write("Financial Analysis\n")
    csvfile_out.write("-----------------------------\n")
    csvfile_out.write(f"Total Months: {numOfMonths}\n")
    csvfile_out.write(f"Total: ${totalLossGain}\n")
    csvfile_out.write(f"Average Change: ${round(totalChange / (numOfMonths - 1), 2)} \n")
    csvfile_out.write(f"Greatest Increase in Profits: {biggestGainMonth} (${biggestGain})\n")
    csvfile_out.write(f"Greatest Decrease in Profits: {biggestLossMonth} (${biggestLoss})\n")