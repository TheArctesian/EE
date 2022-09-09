from coalas import csvReader as c 

def buy(price, balance, btc):
    if balance == 0:
        return btc
    if balance > price: 
        btc = balance/price
    if price > balance:
        btc = price/balance
    return btc

def sell(price, balance, btc):
    if btc == 0:
        return balance
    balance = price*btc 
    return balance



c.importCSV('../Qual/bayes/daddybayes/classified.csv')
c.printHeaders()
balance = 0
btc = 1
netBal = 11766

c.addCol("out")
for i in range(len(c.action)):
    act = int(c.action[i])
    price = int(c.Price[i])

    if act== 0: # None 
            netBal = btc*price
            netBal += balance
            print(balance)
            c.out.append(netBal)
    if act == 1: 
            btc = buy(price, balance, btc)
            balance = 0
            netBal = btc*price
            netBal += balance
            c.out.append(netBal)
    if act == -1:
            balance = sell(price, balance, btc)
            btc = 0
            netBal = balance
            c.out.append(netBal)


c.writeCSV('out.csv')
