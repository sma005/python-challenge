#This file does the following...

import os
import csv

#Grab the data
csvpath = os.path.join('..','PyBank,','Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

        # Read each row of data after the header
    for row in csvreader:
        print(row)

