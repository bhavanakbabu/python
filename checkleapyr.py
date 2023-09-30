currentyear=int(input("enter the currentyear"))
finalyear=int(input("enter the finayear"))
year=currentyear
for year in range(currentyear,finalyear+1,1):
    if(year%4==0 and year%100!=0)or(year%400==0) or (year%100==0 and year%400==0):
        print("the year is leap year",year)
    else:
        print("it not is leap year",year)
        

