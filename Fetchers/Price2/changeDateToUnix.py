import datetime
import pandas
import matplotlib.pyplot as plt
import numpy as np
import ciso8601
def convertMonth(month):
    match month: 
        case "Jan":
            return "01";
        case "Feb":
            return "02";
        case "Mar":
            return "03";
        case "Apr":
            return "04";
        case "May":
            return "05";
        case "Jun":
            return "06";
        case "Jul":
            return "07";
        case "Aug":
            return "08";
        case "Sep":
            return "09";
        case "Oct":
            return "10";
        case "Nov":
            return "11";
        case "Dec":
            return "12";

def parseDate(data):
    array = data.split(" ")
    month = convertMonth(array[0])
    day = array[1].replace(",", "")
    year = array[2]
    dt = datetime.datetime(int(year), int(month), int(day))
    timestamp = dt.replace(tzinfo=datetime.timezone.utc).timestamp()
    return timestamp 

if __name__ == "__main__":

    data = pandas.read_csv('bit.csv')
    for i in reversed(
        range(len(data.Date))):
        temp = str(parseDate(data.Date[i]))
        data.replace(data.Date[i], temp, True)
        print(data.Date[i])
    data.to_csv('out.csv', 
                 index = True)
