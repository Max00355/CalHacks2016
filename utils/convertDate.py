from dateutil import parser
import toDate
import datetime
def convertDate(date):

    print(date)

    try:
        date = parser.parse(date)
    except:
        return None

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

