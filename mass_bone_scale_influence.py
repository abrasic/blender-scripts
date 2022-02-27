# In pose mode, all selected bones will have no scale inheritance to its children.

toInherit = "NONE"
#-------------------
import bpy 
armature = bpy.context.active_object
bones = bpy.context.selected_pose_bones

if bpy.context.mode == "POSE":
    for bone in bpy.context.selected_pose_bones:
        armature.data.bones[bone.name].inherit_scale = toInherit
