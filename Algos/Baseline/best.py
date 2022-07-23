from coalas import csvReader as c

def best(num, num1):
    if num > num1: 
        return -1 # Sell 
    if num == num1: 
        return 0 # Nothing 
    if num < num1:
        return 1 # Buy

def worst(num, num1):
    if num > num1: 
        return 1 # Buy
    if num == num1: 
        return 0 # Nothing 
    if num < num1:
        return -1 # Sell 


if __name__ == "__main__":

    c.importCSV("../Data/Price.csv") 
    c.addCol('Best')
    c.addCol('Worst')
    c.printHeaders()
    for i in range(len(c.Price)):
        if i != 1093:
            b = best(c.Price[i], c.Price[i+1])
            w = worst(c.Price[i], c.Price[i+1])
            c.Best.append(b)
            c.Worst.append(w)
        elif i == 1093:
            c.Worst.append(-1)
            c.Best.append(-1)
    c.writeCSV("check.csv")