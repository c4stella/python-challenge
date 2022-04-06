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

#Setting file path of results file
respath = os.path.join(cwd, 'Analysis', 'results.txt')

#Default value for variables at start of program
moneyTotal = 0
monthTotal = 0
greatestInc = 1
greatestDec = -1

#Reading the csv file
with open(csvpath, encoding='UTF8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    #Skips the header row
    next(csvreader)
    #print(csvreader)
    
    #Looping through each row 
    for row in csvreader:
        #print(row)
        
        timeChange = row[0]
        moneyChange = int(row[1])
            
        #count the sum of both profits and losses
        moneyTotal += moneyChange
        
        #count the total months
        monthTotal += 1
        
        #track the largest positive number as greatest increase, and the month it happened
        if moneyChange > greatestInc:
            greatestInc = moneyChange
            gIncDate = timeChange
        
        #track the largest negative number as greatest decrease, and the month it happened
        if moneyChange < greatestDec:
            greatestDec = moneyChange
            gDecDate = timeChange
        


#find average of changes
avgChange = moneyTotal / monthTotal

#For testing
#print(moneyTotal)
#print(monthTotal)
#print(avgChange)
#print(greatestInc)
#print(greatestDec)

#Final output
result = f'''
````text
Financial Analysis
Total: {moneyTotal}
Total Months: {monthTotal}
Average Change: {avgChange}
Greatest Increase in Profit: {greatestInc} on {gIncDate}
Greatest Decrease in Profit: {greatestDec} on {gDecDate}
'''

#Export output as its own txt file
print(result, file=open(respath, 'w'))

#Alternate way to generate txt file
#r = open(respath, mode='w')
#r.write("Analysis complete")
#r.close