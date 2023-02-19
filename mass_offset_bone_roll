# Primarily used for importing FBX files with skeletons, offsets the bone roll by deg_offset for all selected EDIT BONES.
# To use: Modify the deg_offset variable to the offset of your choice, in degrees. Then in edit mode, select all edit bones that will be affected by this script. Then run.

deg_offset = 180

import bpy, math
if bpy.context.mode == "EDIT_ARMATURE" and len(bpy.context.selected_editable_bones) > 0:
    rad = deg_offset * (math.pi/180)
    for bone in bpy.context.selected_editable_bones:
        bone.roll += rad
