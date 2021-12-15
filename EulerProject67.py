import time 
start = time.time()

myfile = open("triangle.txt", "r")
data = myfile.read()

pyr = data.split("\n")
for i in range(len(pyr)):
  pyr[i] = pyr[i].split(" ")
  pyr[i] = [int(numeric_string) for numeric_string in pyr[i]]

#should try bottom-up
layer = 98
maxi=0

while layer >= 0:
  pathmax = []
  for i in range(len(pyr[layer])):
    pathmax.append(max(int(pyr[layer+1][i]), int(pyr[layer+1][i+1])) + int(pyr[layer][i]))
  pyr.pop()
  pyr.pop()
  pyr.append(pathmax)
  layer-=1

elapsed = (time.time() - start)
print ("found %s in %s seconds" % (pyr[0][0],elapsed))
