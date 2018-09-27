#!/usr/bin/python
import os
import csv

total_vote=0
#candidate=[]
#candidate_per=0
candidate_max=0
x = {}
csv_os = os.path.join("PyPoll_Resources_election_data.csv")
with open(csv_os, 'r') as csvpypoll:
    csv_reader = csv.reader(csvpypoll, delimiter=',')
    csv_header = next(csv_reader)
    
    for i in csv_reader:
        total_vote = total_vote + 1
        x[i[2]] = x[i[2]] + 1 if i[2] in x else 1

    print("Election Results")
    print("Total Votes: " + str(total_vote))

    for i,v in list(x.items()):
        print("%s: %.03f%% (%d)" % (i, round((float(v)*100/total_vote),3), v))
        
        if candidate_max < v:
            candidate_max = v
            candidate_win = i

    print("Winner: " + candidate_win)

    
    