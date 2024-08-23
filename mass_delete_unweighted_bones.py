# Selecting BOTH a mesh and an armature, this script deletes all bones from the armature that do not contain a matching vertex group in the selected mesh.

import bpy
arm = None
weights = None

for obj in bpy.context.selected_objects:
    if not arm and obj.type == "ARMATURE":
        arm = obj
    if not weights and obj.type == "MESH":
        weights = obj.vertex_groups
        
if arm and weights:
    bones = arm.data.edit_bones
    m = bpy.context.mode
    if m != "EDIT":
        bpy.ops.object.mode_set(mode="EDIT")
    for bone in bones:
        if bone.name in weights:
            pass
        else:
            bones.remove(bone)    
    bpy.ops.object.mode_set(mode=m)
else:
    print("No armature and mesh found in selection")
