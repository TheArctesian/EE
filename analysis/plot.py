import pandas
import matplotlib.pyplot as plt
import numpy as np
import os
import time 
import datetime
import ciso8601
data = pandas.read_csv('bit.csv')
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
    tempTime = str(month) + str(day) + str(year)
    print(tempTime)
    ts = ciso8601.parse_datetime(tempTime)
    print(ts)
# Load data
# data = pandas.read_csv('bit.csv')
# print(data.Date)

if __name__ == "__main__":
    # agrument = "Jan"
    # data = pandas.read_csv('bit.csv')
    #for i in range(len(data.Date)):
     #   print(parseDate(data.Date[i]))
    # print(convertMonth(agrument))
    t = "01/12/2011"
    ts = ciso8601.parse_datetime(t)