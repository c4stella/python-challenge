#Importing os module
import os
#Importing csv module
import csv

#Obtaining current working directory
cwd = os.getcwd()
#print(cwd)

#Setting file path of desired csv file
csvpath = os.path.join(cwd, 'Resources', 'budget_data.csv')
#print(csvpath)




with open(csvpath, encoding='UTF8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    for row in csvreader:
        print(row)

