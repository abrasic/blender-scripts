# In pose mode, bones will be renamed including a number based on the order of selection. Useful for renaming joints quicker with large bone counts such as tails, fingers, etc.
# To use, select bones that you would like to rename. Type in your prefix and suffix then execute. SELECTION ORDER MATTERS!

prefix = "tail" # String that will always be included in the name before the number
suffix = ""  # String that will always be included in the name after the number.

import bpy

if bpy.context.mode == "POSE":
    for i, bone in enumerate(bpy.context.selected_pose_bones):
        bone.name = ""
        bone.name = str(prefix) + str(i+1) + str(suffix)
