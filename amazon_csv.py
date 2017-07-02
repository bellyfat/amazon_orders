import csv

def parsecsv(file, filter, text):
    with open(file, newline='') as csvfile:
        myorders = []
        ordersreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        headerrow = next(ordersreader)
        filterindex = headerrow.index(filter)
        for row in ordersreader:
            if (filterrowout(text, filterindex, row) == False):
                myorders.append(row)
        return myorders

def filterrowout(text, filterindex, row):
    if (row[filterindex] == text):
        return True
    else:
        return False

file = 'orders.csv'
filterby = 'Payment Instrument Type'
myfilter = ''
mylist = parsecsv(file, filterby, myfilter)
print(mylist)
                
        

    
