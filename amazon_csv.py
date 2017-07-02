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

def gettotals(myorders):
    mytotal = []
    for order in myorders:
        total = order[len(order) -3].replace('$', '')
        mytotal.append(total)
    return mytotal

file = 'orders.csv'
filterby = 'Payment Instrument Type'
myfilter = ''
myparsedlist = parsecsv(file, filterby, myfilter)              
mytotallist = gettotals(myparsedlist)
print(mytotallist)      




    
