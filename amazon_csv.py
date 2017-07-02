import csv
with open('orders.csv', newline='') as csvfile:
    ordersreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    firstrow = next(ordersreader)
    print(firstrow)
