import time
start = time.time()

myfile = open("names.txt", "r")
data = myfile.read()
data = data.replace('"', "")
names = sorted(data.split(","))
values = {"A": 1, "B": 2, "C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
totalsum=0
for i in range(len(names)):
  namesum=0
  current = names[i]
  for letter in current:
    namesum+=values[letter]
  totalsum += namesum * (i+1)

elapsed = (time.time() - start)
print ("found %s in %s seconds" % (totalsum,elapsed))
