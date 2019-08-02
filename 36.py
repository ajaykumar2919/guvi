aj=input()
count=0
for i in range(len(aj)):
 if(aj[i].isdigit() or aj[i].isalpha() or aj[i]==(" ")):
  continue
 else:
  count+=1
print(count)
