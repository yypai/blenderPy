import bpy
from bpy import context



with open('/Users/name/Desktop/1D-DW/Polar.00001000.dat') as f:
     read_data = f.readlines()

data = [list(map(float, line.split())) for line in read_data] 

head = data[0]
del data[0]


#for i in range (10):

#data = [[1,1,1],[1,1,1]]

for insta in data:
    bpy.ops.mesh.primitive_cone_add(location=(insta[0],insta[1],insta[2]))
