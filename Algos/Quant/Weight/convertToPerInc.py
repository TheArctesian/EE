from coalas import csvReader as c

def percentIncrease(newNumber, oldNumber):
    inc = newNumber - oldNumber
    perinc = inc/oldNumber *100
    return perinc

def makeNew(orgArry):
    perArray = []
    for x in range(len(orgArry)):
        perArray.append(percentIncrease(int(orgArry[x]), int(orgArry[x-1]))) 
    return perArray

if __name__ == "__main__": 
    c.importCSV('../../Data/AllData.csv')
    c.printHeaders()
    priceInc = makeNew(c.Price)
    tradeInc = makeNew(c.TradeVolume)
    transInc = makeNew(c.TransactionsVolume)
    hashrateInc = makeNew(c.HashRate)

    c.TradeVolume = tradeInc
    c.TransactionsVolume = transInc
    c.HashRate = hashrateInc
    c.Price= priceInc
    c.writeCSV('PerInc.csv')