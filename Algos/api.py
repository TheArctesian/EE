import random
from coalas import csvReader as c

fileName = 'file'

def calAction(string)
    if string == 'Buy'
        return 1
    if string == "Sell"
        return 2
    if string == "Hold"
        return 0

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

    
balance = 0
btc = 1
netBal = 11766
print("price,balance,btc,action,netBalance")
for i in data["Price"]:
    action = random.randint(0,2)
    if action == 0: 
        netBal = btc*i
        netBal += balance
        print(f"{i},{balance},{btc},None,{netBal}")
    if action == 1: #you wont be able to buy anything on turn 1
        btc = buy(i, balance, btc)
        balance = 0
        netBal = btc*i
        netBal += balance
        print(f"{i},{balance},{btc},Buy,{netBal}")
    if action == 2:
        balance = sell(i, balance, btc)
        btc = 0
        netBal = btc*i 
        netBal += balance
        print(f"{i},{balance},{btc},Sell,{netBal}")

