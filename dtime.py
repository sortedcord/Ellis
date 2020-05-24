import datetime
from voice import say

def get_today_date():
    now = datetime.datetime.now()  # Since it would be silly to take an argument

    # Control flow for display only!!
    if int(now.day) == 1:
        sl = "st"
    elif int(now.day) == 2:
        sl = "nd"
    elif int(now.day) == 3:
        sl = "rd"
    elif int(now.day) >= 4:
        sl = "th"
    else:
        sl = "th"
    # Control flow to display month name
    if int(now.month) == 1:
        month = "January"
    elif int(now.month) == 2:
        month = "February"
    elif int(now.month) == 3:
        month = "March"
    elif int(now.month) == 4:
        month = "April"
    elif int(now.month) == 5:
        month = "May"
    elif int(now.month) == 6:
        month = "June"
    elif int(now.month) == 7:
        month = "July"
    elif int(now.month) == 8:
        month = "August"
    elif int(now.month) == 9:
        month = "September"
    elif int(now.month) == 10:
        month = "October"
    elif int(now.month) == 11:
        month = "November"
    elif int(now.month) == 12:
        month = "December"
    else:
        # Rare chance, to show an error in  code
        month = "Error 858"

    # Say the whole thing
    say("Today is " + str(now.day) + " of " + month + str(now.year))



nows = datetime.datetime.now()
