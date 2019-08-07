from itertools import combinations
aj,p=list(input().split())
a=[]
p=int(p)
length=combinations(aj,len(aj)-p)
for i in length:
  a.append("".join(i))
print(min(a))
