r,v=map(int,input().split())
for i in range(r+1,v):
  c=i
  fd=0
  while (i>0):
    ar=i%10
    fd=fd+(ar**3)
    i=i//10
    if(fd==c):
      print(fd,end=" ")
