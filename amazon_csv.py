from csvparser import parsecsv
from orderlistutils import *

def ordertotal(myfile): 
    filterby = 'Payment Instrument Type'
    myfilter = ''
    myparsedlist = parsecsv(myfile)  
    myfilterdlist = filterorderlist(myparsedlist, filterby, myfilter) 
    ordercolumn = getordercolumn(myparsedlist)           
    mytotal = getordertotal(myfilterdlist, ordercolumn) 
    return mytotal

ordtot = 0
ordtot += ordertotal('orders2017.csv')
ordtot += ordertotal('orders2016.csv')
ordtot += ordertotal('orders2015.csv')
ordtot += ordertotal('orders2014.csv')
print(ordtot)