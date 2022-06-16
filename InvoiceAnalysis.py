# Program to analyze the age of an invoice.

import datetime
print()
print("Invoice Analysis Program")
print()
Company = input("   Enter the name of the company: ")
InvDate = input("   Enter the date of the invoice (YYYY-MM-DD): ")
InvAmt = float(input("   Enter the amount of the invoice: "))

CurDate = datetime.datetime.now()
InvDate = datetime.datetime.strptime(InvDate, "%Y-%m-%d")
Age = (CurDate - InvDate).days
DisDate = InvDate + datetime.timedelta(days=10)
DueDate = InvDate + datetime.timedelta(days=30)
DisDue = InvAmt * .98

print()
print("   The current date is " + CurDate.strftime("%Y/%m/%d"))
print("   The Invoice Date is " + InvDate.strftime("%Y/%m/%d"))
print()
print("   The invoice is " + str(Age) + " days old.")

if Age <= 30:
    print("      Advice: OK for now")
elif Age >= 31 and Age <= 60:
    print("      Advice: Better think about paying.")
elif Age > 60:
    print("      Advice: This one could be in trouble.")

print()
print("   Based on the common terms of 2/10N30")
print("     The discount period ends on " + DisDate.strftime("%Y/%m/%d"))
print("     The amount due before the discount date is ${:,.2f}".format(DisDue))
print("     The invoice total is due by " + DueDate.strftime("%Y/%m/%d"))
print()

Anykey = input("Press any key to continue.")
