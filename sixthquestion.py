a=int(input())
def show_stars(x):
  for i in range (1,x+1):
    for j in range (1,i+1):
      print("*",end="")
    print("\r")
show_stars(a)


