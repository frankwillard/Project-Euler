import time 
start = time.time()

num = 100 * 100
palindromes = []
while num < 999 * 999:
  string = str(num)
  if len(string) % 2 == 0:
    if string[0:3] == string[3:6][::-1]:
      palindromes.append(num)
  else:
    if string[0:2] == string[3:5][::-1]:
      palindromes.append(num)
  num+=1

for i in range(0,len(palindromes)):
  for j in range(100,999):
    if palindromes[i] % j == 0:
      if len(str(int(palindromes[i]/j))) == 3:
        largest = palindromes[i]
elapsed = (time.time() - start)
print ("found %s in %s seconds" % (largest,elapsed))
