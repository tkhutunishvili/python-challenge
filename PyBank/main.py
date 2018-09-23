import os
import csv

with open ("PyBank_Resources_budget_data.csv", 'r') as csvpypoll:
    csv_reader = csv.DictReader(csvpypoll, delimiter=',')
    month_count = 0
    total = 0
    min_change = None
    max_change = None
    min_change_m = None
    max_change_m = None
    change_total = 0
    for i in csv_reader:
        #print(i)
        month_count = month_count + 1
        cur = int("{Profit/Losses}".format(**i))
        total = total + cur
        if month_count == 1:
            min_value = cur
            max_value = cur
            prev = cur
        else:
            if cur < min_value:
                min_value = cur
            if cur > max_value:
                max_value = cur
            change = cur - prev
            change_total = change_total + change
            if not min_change or (change < min_change):
                min_change = change
                min_change_m = "{Date}".format(**i)
            if not max_change or (change > max_change):
                max_change = change
                max_change_m = "{Date}".format(**i)
        prev = cur
    print("Total Months: " + str(month_count))
    print("Total: " + str(total))
    print("Average  Change:",round(change_total / (month_count-1),2))
    print("Greatest Increase in Profits:",max_change_m,max_change)
    print("Greatest Decrease in Profits:",min_change_m,min_change)

# 10 = 10
# 20 = 20-10 = 10
# 5  = 5-20 = -15
# 15 = 15-5 = 10