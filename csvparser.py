import csv

def parsecsv(filename):
    with open(filename, newline='') as csvfile:
        parsedcsv = []
        ordersreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in ordersreader:
            parsedcsv.append(row)
        return parsedcsv