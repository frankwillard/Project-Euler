import time 
start = time.time()
sundays = 0
months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
month = 1
year = 1901

totalday = 0
while year < 2001:
  if totalday % 7 == 0:
    sundays+=1
  totalday += months[month]
  if month == 2 and year % 4 == 0:
    totalday+=1
  month+=1
  if month == 13:
    month = 1
    year+=1

elapsed = (time.time() - start)
print ("found %s in %s seconds" % (sundays,elapsed))
