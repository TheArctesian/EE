from coalas import csvReader as c 

def checkSim(array, value):
    # check if value is in array
    if value in array: 
        return False
    if value not in array: 
        return True

def calAvg(array):
    t = 0
    for i in array: 
        t += int(i)
    print(t)
    return t

def convertToAction(number):
    if number == 0:
        return 0
    if number > 0:
        return 1
    if number < -1:
        return -1
    else:
        return 0

if __name__ ==  "__main__":
    c.importCSV("test.csv")

    c.printHeaders()

    time = []
    price = []
    for i in range(len(c.date)):
        if checkSim(time, c.date[i]):
            time.append(c.date[i])
            price.append(c.price[i])
    action = []
    for i in time: 
        tempAction = []
        for x in range(len(c.date)):
            if c.date[x] == i:
                tempAction.append(c.action[x])


        a = (calAvg(tempAction))
        act = convertToAction(a)
        action.append(act)
    
    with open("classified.csv", "w") as f: 
        f.write("date,action,price\n")
        for i in range(len(time)):
            f.write(f'{time[i]},{action[i]},{price[i]}\n') 
    
