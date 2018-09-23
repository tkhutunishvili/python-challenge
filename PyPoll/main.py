import os
import csv

csv_os = os.path.join("PyPoll_Resources_election_data.csv")
with open(csv_os, 'r') as csvpypoll:
    csv_reader = csv.reader(csvpypoll, delimiter=',')
    print(csv_reader)