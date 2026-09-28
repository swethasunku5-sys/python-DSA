def range_sum(a,st,end):
  return a[end]-a[st-1]
def prefixarray(a):
  prefix = [0] * len(a)
  prefix[0] = a[0]
  for i in range(1, len(a)):
    prefix[i] = prefix[i-1] + a[i]
  return prefix

a=[3, 1, 4, 1, 5, 9, 2, 6]
prefix=prefixarray(a)
print(prefix)
print(range_sum(prefix,2,5))
#subb=array sum equals to target
def sumarray(a,k,target):
  s=0
  if k<=0 or k>len(a):
    return 'invalid key elements'
  for  i in range(k):
    s+=a[i]
  if s==target:
    return [a[i] for i in range(k)]
  for i in range(k,len(a)):
    s=s+a[i]-a[i-k]
    if s==target:
      return [a[i] for i in range(i-k+1,i+1)]
  return -1    
print(sumarray(a,3,10))