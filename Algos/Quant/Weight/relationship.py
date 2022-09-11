from coalas import csvReader as c

def dif(price, value):
    return price-value
def avg(array):
    s = 0
    for i in array:
        s+= i    
    print(s)
def makeNew(orgArray):
    empty=[]
    for i in range(len(orgArray)):
        empty.append(dif(float(c.Price[i]), float((orgArray[i]))))
    return empty
if __name__ == "__main__": 
    c.importCSV('PerInc.csv')
    tradeInc = makeNew(c.TradeVolume)
    transInc = makeNew(c.TransactionsVolume)
    hashrateInc = makeNew(c.HashRate)
    avg(tradeInc)
    avg(transInc)
    avg(hashrateInc)
    c.TradeVolume = tradeInc
    c.TransactionsVolume = transInc
    c.HashRate = hashrateInc
    c.writeCSV('difInce.csv')

# trade: -18514.93252201425
# trans: -746.1249763132469
# harshrate: 32.05882406901156