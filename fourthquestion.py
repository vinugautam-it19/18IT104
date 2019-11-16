a=int(input())
def shownumbers(x):
  for i in range(x+1):
    if(i%2==0):
      print("EVEN",i)
    else:
      print("ODD",i)
shownumbers(a)
