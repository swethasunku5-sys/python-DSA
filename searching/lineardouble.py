#linear search
def linearsearch(a,el):
  ar=[]
  for i in range(len(a)):
    if a[i]==el:
      
      ar.append(i)
  return ar

a=[12,2,44,23,14,65,14]
print(linearsearch(a,14))