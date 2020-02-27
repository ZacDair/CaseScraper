import urllib.request
from datetime import date
# Steam Date Format = Oct 03 2019
# Datetime Format = 2019-10-03


# Get actual date and change it to the format Steam uses
def getCalenderDate(x):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    dateParts = str(x).split("-")
    month = months[int(dateParts[1])-1]
    yesterday= int(dateParts[2]) - 1
    if len(str(yesterday)) == 1:
        newDate = (month + " 0" + str(yesterday) + " " + dateParts[0])

    else:
        newDate = (month + " " + dateParts[2] + " " + dateParts[0])

    return newDate


# Get today's date, and run getCalenderDate, open our url, split content by date
def getItemPrices(url):
    todayDate = getCalenderDate(date.today())
    with urllib.request.urlopen(url) as url:
        contents = url.read()
        res = (str(contents).split(str(todayDate)))

    # ignore first and last (index 0 and len(res)) as they don't contain price information
    i = 1
    prices = []
    while i < len(res)-1:
        temp = (res[i].split(","))
        prices.append(temp[1])
        i = i + 1

    # Get average price
    avg = 0
    for p in prices:
        avg = avg + float(p)
    avg = avg / len(prices)
    print("The average for " + todayDate + " is " + str(round(avg, 3)) + "$")
