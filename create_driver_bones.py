# CREATE DRIVER BONES v1
# ---------------------------------
# How to use: Go into Edit Mode and select the bones that you want to make driver bones for.
# The driver bones will be placed on the second bone layer.

# What's the point?
# This script is primarily used for fingers and wings and removes the tedious work of manually creating bones and constraints.
# Since driver vaules cannot be offset directly, we will make a "driver bone" to place all the drivers on,
# then a Copy Rotation constraint will be added so we can add extra rotation if necessary.

preferred_rotation_mode = "XYZ" # The rotation to be set on selected bones and driver bones. Euler is preferred.



#----------------------------------
import bpy


armature = bpy.context.active_object
bones = bpy.context.selected_bones

# Only run if user is in Edit Mode, has at least one bone selected and target is an armature
if bpy.context.mode == "EDIT_ARMATURE" and bones and armature.type == "ARMATURE":
    for bone in bones: # Check if a driver bone already exists for this bone
        try:
            bpy.context.active_object.data.bones[bone.name + ".Driver"]
        except KeyError: # Create driver bone
            driverBone = armature.data.edit_bones.new(bone.name + ".Driver")
            driverBone.length = bone.length
            driverBone.matrix = bone.matrix.copy()
            driverBone.parent = bone.parent
            
            # Move to second bone layer
            driverBone.layers[1] = True
            driverBone.layers[0] = False
        else:
            print("Driver bone already exits, skipping")
            
    bpy.ops.object.mode_set(mode='POSE')
    
    poseBones = bpy.context.selected_pose_bones
    for bone in poseBones:
        
        # Delete existing constraints on selected bones, if any
        if len(bone.constraints) > 0:
            for constraint in bone.constraints:
                bone.constraints.remove(constraint)
        
        # Set rotation mode
        bone.rotation_mode = preferred_rotation_mode
        bpy.context.active_object.pose.bones[bone.name + ".Driver"].rotation_mode = preferred_rotation_mode
        
        # Create constraint onto main bone
        rotConst = bone.constraints.new(type='COPY_ROTATION')
        rotConst.target = armature
        rotConst.subtarget = bone.name + ".Driver"
        rotConst.mix_mode = 'ADD'
        rotConst.target_space = 'LOCAL'
        rotConst.owner_space = 'LOCAL'
