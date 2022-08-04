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

def eng(name):
    c.addCol(name)
    balance = 0
    btc = 1
    netBal = 11766
    for i in range(len(c.Price)): 
        action = c.action[i]
        print(f'{action} + {type(action)}')
        if action == '0': # None 
            netBal = btc*c.Price[i]
            netBal += int(balance)
            print(balance)
            print(action)
            c.balance.append(balance)
        if action == '1': #you wont be able to buy anything on turn 1
            btc = buy(c.Price[i], balance, btc)
            balance = 0
            netBal = btc*c.Price[i]
            netBal += int(balance)
            print(balance)
            print(action)
            c.balance.append(balance)
        if action == '-1':
            balance = sell(c.Price[i], balance, btc)
            btc = 0
            netBal = int(balance)
            print(balance)
            print(action)
            c.balance.append(balance)


if __name__ == "__main__":
    c.importCSV('../Qual/bayes/daddybayes/classified.csv')
    eng("balance")
    c.printHeaders()
    c.writeCSV("out.csv")
