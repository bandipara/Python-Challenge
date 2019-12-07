
##PyBANK

import os
import csv
import sys



#csvpath = os.path.join("Resources", "netflix_ratings.csv")
csvpath = os.path.join("D:\Rutgers-lab\Homework\Python-Challenge\PyBank","Resources", "budget_data.csv")
#print(csvpath)

count = 0
total = 0
average= 0
max_num = 0
min_num = 0
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        count += 1
        total += int(row[1])
        average = total/count
    

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    d_col = list(csvreader)

    min_row = min(d_col, key=lambda row: float(row[1]))
    max_row = max(d_col, key=lambda row: float(row[1]))


sys.stdout = open(os.path.join(sys.path[0], "PyBank_Output.txt"), "w")

print("Greatest Increase in Profits: ", min_row)
print("Greatest Decrease in Profits: ", max_row)
#d_col
print (count) #Prints The total number of months included in the dataset
print(total)   #Prints The net total amount of "Profit/Losses" over the entire period
print(average) #Prints The average of the changes in "Profit/Losses" over the entire period
#python "main.py" >> "output.txt"