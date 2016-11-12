import datetime
from dateutil import parser

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
endings = {1: 'st', 2: 'nd', 3: 'rd'}

def toDate(date):
    date = parser.parse(date)
    ending = "th"
    if date.day == 1:
        ending = endings[1]
    elif date.day == 2:
        ending = endings[2]
    elif date.day == 3:
        ending = endings[3]

    outputText = months[date.month] + " " + str(date.day) + ending + ", " + str(date.year) + " " + amOrPm(date.hour, date.minute)
    return outputText

def amOrPm(hour, minute):
    hourMinuteString = "{}:{}".format(hour, minute)
    d = datetime.datetime.strptime(hourMinuteString, "%H:%M")
    return d.strftime("%I:%M %p")
