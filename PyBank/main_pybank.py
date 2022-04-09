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
values = []
months = []
diffValues = []

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
        
        #log all movements in value into list for further iteration
        values.append(moneyChange)
        
        #log all months into list for further iteration
        months.append(timeChange)
    
    #Looping through all values, making sure to not include the first month
    for i in range(len(values) - 1):
        
        #log the differences in total value between each month to list
        diffValues.append(values[i] - values[i - 1])
        greatestInc = max(diffValues)
        greatestDec = min(diffValues)

    #Looping through list of months
    for m in range(len(months)):
        
        #Match the index of the greatest change to its respective index in months
        gIncDate = months[diffValues.index(greatestInc)]
        gDecDate = months[diffValues.index(greatestDec)]
        

#find average of changes
avgChange = round(sum(diffValues) / (monthTotal - 1), 2)

#Final output
result = f'''
Financial Analysis
Total: ${moneyTotal}
Total Months: {monthTotal}
Average Change: ${avgChange}
Greatest Increase in Profit: ${greatestInc} on {gIncDate}
Greatest Decrease in Profit: ${greatestDec} on {gDecDate}
'''

#Export output as its own txt file
print(result, file=open(respath, 'w'))