import time 
start = time.time()

sum=0
palindromes = []
for n in range(1000000):
  string = str(n)
  if len(string) % 2 == 0:
    if string[0:int(len(string)/2)] == string[int(len(string)/2):len(string)][::-1]:
      palindromes.append(n)
  else:
    if string[0:int(len(string)/2)] == str(string[int(len(string)/2)+1:len(string)])[::-1]:
      palindromes.append(n)

for i in range(len(palindromes)):
  binary = str(bin(palindromes[i]))
  binary = binary[2:len(binary)]
  if len(binary) % 2 == 0:
    if binary[0:int(len(binary)/2)] == binary[int(len(binary)/2):len(binary)][::-1]:
      sum+=palindromes[i]
  else:
    if binary[0:int(len(binary)/2)] == binary[int(len(binary)/2)+1:len(binary)][::-1]:
      sum+=palindromes[i]

elapsed = (time.time() - start)
print ("found %s in %s seconds" % (sum,elapsed))
