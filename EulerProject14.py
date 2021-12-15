highest = 508
def sequence(n):
  count = 0
  while n != 1:
    if n % 2 == 0:
      n = n/2
    else:
      n = 3*n + 1
    count+= 1
  return count

for n in range(800000,1000000):
  memoize = sequence(n)
  if memoize > highest:
    highest = memoize
    index = n
print(index)
