import bpy
from mathutils import Vector
from mathutils import Matrix
import math

with open('/Users/yun-yi/Desktop/1D-DW/Polar.00001000.dat') as f:
     read_data = f.readlines()

df = [list(map(float, line.split())) for line in read_data] 

head = df[0]
del df[0]



ob = bpy.context.view_layer.objects.active
obs = []
sce = bpy.context.view_layer

for i in df:

    copy = ob.copy()
    copy.location += Vector((i[0] - 1, i[1] - 1, 2*(i[2] - 1)))
    copy.rotation_euler = (i[2]/10*3.14, 0, 0)
    copy.data = copy.data.copy() # also duplicate mesh, remove for linked duplicate
    obs.append(copy)
    
    
    


# copy.rotation_euler = (obj.rotation_euler.to_matrix() * Matrix.Rotation(math.pi, 3, 'Z')).to_euler

for ob in obs:
    bpy.context.collection.objects.link(ob)


bpy.context.view_layer.update()
