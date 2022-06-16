# Comment like a pro.

import datetime

CurDate = datetime.datetime.today()
ChrDate = datetime.datetime(CurDate.year, 12, 25)
if CurDate.month == 12 and CurDate.day > 25:
    ChrDate = datetime.datetime(CurDate.year + 1, 12, 25)
DaysToChr = (ChrDate - CurDate).days

print()
print("The current date is " + CurDate.strftime("%Y/%m/%d"))
print("The next Christmas day is on " + ChrDate.strftime("%Y/%m/%d"))
print("There are " + str(DaysToChr) + " days to Christmas")
print()

Anykey = input("Press any key to continue.")

