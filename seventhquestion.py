a=int(input())
def limit(x):
  count=0
  for i in range(1,x+1):
    for j in range(1,x+1):
      if(i%j==0):
        count=count+1
    if (count==2):
      print(i,end=",")
    count=0
limit(a)
