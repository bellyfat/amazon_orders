def getfiltercolumnindex(columntext, orderheaderlist):
    return orderheaderlist.index(columntext)

def getordercolumn(orderlist):
    headerlist = list(orderlist).pop(0)
    return getfiltercolumnindex('Total Charged', headerlist)

def filterrowout(row, filterindex, text):
    return bool(row[filterindex] == text)

def gettotallist(myorders, ordercolumn):
    mytotal = []
    for order in myorders:
        total = order[ordercolumn].replace('$', '')
        mytotal.append(total)
    return mytotal

def sumtotal(totallist):
    total = 0
    for price in totallist:
        total += float(price)
    return total

def getordertotal(myorders, ordercolumn):
    totallist = gettotallist(myorders,ordercolumn)
    return sumtotal(totallist)

def filterorderlist(orderlist, filterby, filtertext):
    orders = []
    orderlist = list(orderlist)
    headerlist = orderlist.pop(0)
    filterindex = getfiltercolumnindex(filterby, headerlist)
    for row in orderlist:
        if not filterrowout(row, filterindex, filtertext):
            orders.append(row)
    return orders