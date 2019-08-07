n=int(input())
a=[]
for x in range(0,n):
 la=input()
 a.append(la)
new=[]
for x in zip(*a):
 if(x.count(x[0])==len(x)):
  new.append(x[0])
 else:
  break
print(''.join(new))
