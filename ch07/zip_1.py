x=['a','b','c']
y=[1,2,3]
z=[]

for i, f in zip(x,y):
    z.append(i)
    z.append(f)
print(z)