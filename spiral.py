import bpy
from bpy import context
import math

data = []

for i in range (100):
    data.append([-i*math.cos(0.3*i), -i*math.sin(0.3*i), 2*0.3*i])
    
for k in range (99):
    for i in range (99-k):
        for j in range(3):
            data[i+1+k][j] = data[i+1+k][j] - data[0+k][j]




#for i in range (10):

#data = [[1,1,1],[1,1,1]]

for insta in data:
    bpy.ops.mesh.primitive_cone_add(location=(insta[0],insta[1],insta[2]))
