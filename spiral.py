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

for yla in data:
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":yla, "constraint_axis":(False, False, False), "mirror":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
