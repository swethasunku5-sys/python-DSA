n=int(input())
a=list(map(int,input().split(' ')))
sumvalue=0
for i in a:
  sumvalue+=i
res=sumvalue/n
print(res)
print(f'{res:.2f}')