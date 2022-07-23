
from coalas import csvReader as c
import datetime
import time

def toUnix(date):
    x = date.split('-')
    t = datetime.date(int(x[0]),int(x[1]),int(x[2]))
    unix = time.mktime(t.timetuple())
    return unix

if __name__ == "__main__":
    start_time = time.time()
    c.importData('new.csv')
    c.addCol('unixTime')
    c.printHeaders()
    for i in range(len(c.date)):
        d = c.date[i] 
        unix = toUnix(d)
        c.unixTime.append(unix)
    print("--- %s seconds --- Sort Start" % (time.time() - start_time))
    sort_time =time.time()
    c.sort(c.unixTime, 'acc')
    c.writeCSV("p.csv")
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s sort ---" % (time.time() - sort_time))