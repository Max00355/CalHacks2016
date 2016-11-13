from dateutil import parser
import toDate
import datetime
def convertDate(date):

    print("date below")
    print(date)
    print("date above")

    try:
        date = parser.parse(date)
    except:
        mydate = datetime.datetime.now()
        out = "{}-{}-{}".format(mydate.year, mydate.month, mydate.day)
        return out

    if (date - datetime.datetime.now()).days < 0:
        increment = True
    else:
        increment = False
    month = "0{}".format(date.month) if date.month < 10 else date.month
    day = "0{}".format(date.day) if date.day < 10 else date.day
    if increment:
        out = "{}-{}-{}".format(date.year + 1, month, day)
    else:
         out = "{}-{}-{}".format(date.year, month, day)       
    return out

