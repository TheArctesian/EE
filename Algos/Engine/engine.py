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

def eng(array, name):
    c.addCol(name)
    balance = 0
    btc = 1
    netBal = 11766
    for i in range(len(c.Price)): 
        action = array[i]
        action = int(action)
        if action == 0: # None 
            netBal = btc*c.Price[i]
            netBal += balance
            print(balance)
            print(action)
            c.globals[name].append(balance)
        if action == 1: #you wont be able to buy anything on turn 1
            btc = buy(c.Price[i], balance, btc)
            balance = 0
            netBal = btc*c.Price[i]
            netBal += balance
            print(balance)
            print(action)
            c.globals[name].append(balance)
        if action == -1:
            balance = sell(c.Price[i], balance, btc)
            btc = 0
            netBal = balance
            print(balance)
            print(action)
            c.globals[name].append(balance)


if __name__ == "__main__":
    c.importCSV("../Baseline/comp.csv")
    eng(c.Best, "BestTests")
    c.removeCol('TextBlobPol')
    c.removeCol('VaderPol')
    c.removeCol('DictPol')
    c.removeCol('TecAction')
    c.removeCol('Best')
    c.removeCol('Worst')
    c.removeCol('Trained')
    # c.writeCSV("test.csv")
    c.printHeaders()