a=int(input())
def limit(x):
  sum=0
  for i in range (x+1):
    if((i%3==0)or(i%5==0)):
      sum=sum+i
  return sum;
print(limit(a))
