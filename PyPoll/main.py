

import os
import csv
import sys


os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join("Resources", "election_data.csv")


count = 0
candidates_list = []
Sum_vote = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)
    for row in csvreader:
        count += 1
        
        candidate = (row[2])
        
        if candidate in candidates_list:
            candidate_index = candidates_list.index(candidate)
            Sum_vote[candidate_index] = Sum_vote[candidate_index] + 1
        else:
            candidates_list.append(candidate)
            Sum_vote.append(1)



pct = []
max_votes = Sum_vote[0]
max_index = 0

for x in range(len(candidates_list)):
    vote_pct = round(Sum_vote[x]/count*100, 2)
    pct.append(vote_pct)
    
    if Sum_vote[x] > max_votes:
        max_votes = Sum_vote[x]
        max_index = x

election_winner = candidates_list[max_index] 


sys.stdout = open(os.path.join(sys.path[0], "PyPoll_Output.txt"), "w")

print('======================================================')
print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {count}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidates_list)):
    print(f'{candidates_list[x]} : {pct[x]}% ({Sum_vote[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {election_winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
