import csv

def parsecsv(file, filter):
    with open(file, newline='') as csvfile:
        myorders = []
        ordersreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        headerrow = next(ordersreader)
        for row in ordersreader:
            if row != headerrow:
                myorders.append(row)
        return myorders

mylist = parsecsv('orders.csv', '')
print(mylist)
                
        
