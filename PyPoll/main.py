#!/usr/bin/python
import os
import csv
import sys

total_vote=0
candidate_max=0
candidates_dict = {}
csv_os = os.path.join("PyPoll_Resources_election_data.csv")
with open(csv_os, 'r') as csvpypoll:
    csv_reader = csv.reader(csvpypoll, delimiter=',')
    csv_header = next(csv_reader)
    
    for i in csv_reader:
        total_vote = total_vote + 1
        candidates_dict[i[2]] = candidates_dict[i[2]] + 1 if i[2] in candidates_dict else 1
    sys.stdout=open("PyPoll_Resources_election_data.txt","w")
    print("Election Results")
    print("Total Votes: " + str(total_vote))

    for i,v in candidates_dict.items():
        print("%s: %.03f%% (%d)" % (i, round((float(v)*100/total_vote),3), v))
        
        if candidate_max < v:
            candidate_max = v
            candidate_win = i

    print("Winner: " + candidate_win)
    sys.stdout.close()
    
