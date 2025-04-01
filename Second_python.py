# This is my first comment, in my first python true basic app
print( "Mary's dog said \"woof\". ")
print( " Nothing last forever\n But constantness last forever")
x = True; y =True;
print(x)
a = 20;
b=7;
print( "a%b = ", a%b);
print("\n a**b = ", a**b, "\n");
print( " a//b = ", a//b);
c = x and y;
d = False
e = c and d
print("\n c=",c)
print("\n e= ", e)

x =-4
y = abs(x)
print("\n y absolute value is:",y)
x = 3.982379
y= round(x,3)
print("\n y in 3 decimal place is: ",y)
numeric1 = 3.2345996; numeric2 =-5.9567823; numeric3 = -456.88997
print(int(numeric1))
print(round(numeric1))
print(bin(int(numeric1)))
print(max(abs(numeric1), abs(numeric2), abs(numeric3)))
print(round(numeric2,4))
print(hex(round(numeric1)))
import math
print(math.sin(math.cos(math.tan(x))))
formular = " Gm1m2/r^2";
print(f"\n Gravity Formular= {formular}")
osita_salary_annually = 70000;
print(f"\n Osita salary_per_year: ${osita_salary_annually:,.3f}", "in USD")
print(f"\n in Naira is equivalent to: N{1550*osita_salary_annually:,.3f}", "in Naira")
print("\n")



# import datetime and dateutil tz
import datetime as dt
from dateutil.tz import gettz

#utc time zone
utc = dt.datetime.now(gettz('ETC/UTC'))
print(f"{utc:%A %D %I:%M %p %Z }")

#USA eastern time
est=dt.datetime.now(gettz('AMerica/New_york'))
print(f"{est:%A %D %I:%M %p %Z}")

#import datetime as dt
event =dt.datetime(2026,10,1,10,0,0)
print(f"Local Date and time:{event: %D %I:%M %p %Z}" + "\n")

event_eastern = event.astimezone(gettz('America/New_York'))
print(f"{event_eastern: %D %I:%M %p %Z}")

event_central =event.astimezone(gettz('america/Chicago'))
print(f"{event_central: %D %I:%M %p %Z}")

event_mountain = event.astimezone(gettz('America/Denver'))
print(f"{event_mountain: %D %I:%M %p %Z}")
