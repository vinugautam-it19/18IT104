def speed(x):
  if(x<=70):
    c="ok"
  else:
    d=x-70
    e=d//5
    if(e<=12):
      c="point : %d"%e
    else:
      c="your license suspeded"
  return c;
print(speed(80))
print(speed(60))
print(speed(135))
