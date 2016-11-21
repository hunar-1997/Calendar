def is_it_leap(n):
    # determine if it's a leap year of not
    c = (((n%4==0)and(n%100!=0))or(n%400==0))and(n%2800!=0)
    if c:
        return True
    return False

def day_in_week(n):
    # get the year's first day's position in the week
    n -= 1
    r = 0
    r += int(n/4)
    r -= int(n/100)
    r += int(n/400)
    r -= int(n/2800)
    n -= r
    
    n *= 365
    r *= 366
    
    return (n+r+2)%7

def print_calendar(n,c):
    is_leap = is_it_leap(n)
    
    print("\nCalendar for year:", n)
    months=["January", "February", "March",
            "April", "May", "Jun", "July",
            "August", "September", "October",
            "November", "December"]
    
    for i in range(12):
        l = i%7
        if l%2==0:
            l=1
        else:
            l=0
            if i==1:
                if is_leap:
                    l=-1
                else:
                    l=-2
        
        print("\n"+months[i])
        print("Sat Sun Mon Tue Wed Thu Fri")
        
        f=False
        for j in range(30+l):
            if c%7==0 and j!=0:
                print()
            
            if not f:
                print("    "*(c%7), end="")
                f=True
            
            print("{:3}".format(j+1), end=" ")
            c+=1
        
        print()

while True:
    year = int( input("year: ") )
    c = day_in_week(year)
    print_calendar(year, c)
    
    #break



