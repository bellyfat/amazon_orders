from csvparser import parsecsv
from orderlistutils import *

myfile = 'orders.csv'
filterby = 'Payment Instrument Type'
myfilter = ''
myparsedlist = parsecsv(myfile)  
myfilterdlist = filterorderlist(myparsedlist, filterby, myfilter) 
ordercolumn = getordercolumn(myparsedlist)           
mytotal = getordertotal(myfilterdlist, ordercolumn) 
print(mytotal)    




    
