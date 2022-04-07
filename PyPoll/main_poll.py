#Importing os module
import os
#Importing csv module
import csv
#Importing pandas?

#Obtaining current working directory
cwd = os.getcwd()
#print(cwd)

#Setting file path of desired csv file
csvpath = os.path.join(cwd, 'Resources', 'election_data.csv')
#print(csvpath)

totalCount = 0


with open(csvpath, encoding='UTF8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    for row in csvreader:
        #print(row)
        totalCount += 1