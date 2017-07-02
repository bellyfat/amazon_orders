
def filterrowout(text, filterindex, row):
    return bool(row[filterindex] == text)

def gettotalfromorders(myorders):
    mytotal = []
    for order in myorders:
        total = order[len(order) -3].replace('$', '')
        mytotal.append(total)
    return mytotal

def sumtotal(totallist):
    total = 0
    for price in totallist:
        total += float(price)
    return total
