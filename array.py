import numpy as np
matrix = []
rownb = int(input("enter row"))
colnb= int(input("enter col"))
for i in range(rownb):
    a=[]
    for j in range(colnb):
        val=int(input(f"enter value for position ({i+1},{j+1});"))
        a.append(val)
    matrix.append(a)
mar=np.array(matrix)
print(mar)    
