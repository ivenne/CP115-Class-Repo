"""PROGRAMMER'S NAME: IVENNE
    PRBLEM DESCRIPTION: Calculating bill price based on monthly usage and discount """

"Enter monthly usage"
MonthlyUsage = float(input("Enter monthly usage: "))

"Bill price calculation based on monthly usage and discount"
if MonthlyUsage < 50 : 
    BillPrice = MonthlyUsage - (MonthlyUsage * 0)
elif MonthlyUsage <= 100  :
    BillPrice = MonthlyUsage - (MonthlyUsage * 0.05)
else :
    BillPrice = MonthlyUsage - (MonthlyUsage * 0.2)

"Display the bill price"
print (f"Bill Price after diacount is MYR{BillPrice}")