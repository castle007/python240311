import time
# from datetime import *

print(dir(time))

print(time.time())
print(time.gmtime())
print(time.localtime())

from datetime import *
d1 = date(2024, 5,1 )
print(d1)

d2 = date.today()
print(d2)

d3 = datetime.now()
print(d3)

d4 = timedelta(days=100)
print(d2+d4)
print(d2-d4)