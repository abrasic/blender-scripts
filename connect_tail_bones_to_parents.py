# Simple script to quickly retarget the tails of bones to the parent's bone head.
# You must be in edit mode and this will only target the first armature

import bpy

for bone in bpy.data.armatures[0].edit_bones:
    if bone.parent is not None:
        bone.parent.tail = bone.head
