# This script allows you to quickly apply twist bones to automatically drive from a primary deform bone for rigs that have them.
# This is most useful on hands, where rotating them a full 180 can result in a malformed wrist.

# Go in pose mode, execute this script in a Text Editor and locate the menu in the Bone Properties tab.
# The first bone you select will be the target bone. In the example of a hand, you would select the primary hand bone FIRST.
# Then shift select the TWIST bone. You should see the settings for the dropdown appear.

#  TWIST ROTATION: This is the axis that the twist bone will rotate on when the target bone rotates.
# TARGET ROTATION: This is the axis that the twist bone will copy and drive from.
#       INFLUENCE: This is the multiplier of the twist bone. A value of 0.5 will copy half of the target bone's rotation.

# Clicking "Add Quick Drivers" will quickly add the drivers to create a proper twist bone.

import bpy
   
class addQuickDriver(bpy.types.Operator):
    bl_idname = "qt.add_drivers"
    bl_label = "Add Quick Drivers"  
    
    def execute(self, context):
        prefs = bpy.context.scene.quicktwist
        newDriver = bpy.context.selected_pose_bones[1].driver_add('rotation_euler',int(prefs.twistrotation))
        
        for oldVar in newDriver.driver.variables:
            newDriver.driver.variables.remove(oldVar)
            
        var = newDriver.driver.variables.new()
        var.type = "TRANSFORMS"
        
        target = var.targets[0]
        target.id = bpy.context.active_pose_bone.id_data
        target.bone_target = bpy.context.selected_pose_bones[0].name
        target.transform_type = prefs.targetrotation
        
        newDriver.driver.expression = var.name + ' * ' + str(prefs.influence)
        
        bpy.context.selected_pose_bones[1].rotation_mode = "XYZ"
        return {"FINISHED"}

class QuickTwistPanel(bpy.types.Panel):
    bl_label = "Quick Twist Drivers"
    bl_idname = "OBJECT_PT_twist"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "bone"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
        
        targetBone = ""
        twistBone = ""
        if bpy.context.mode == "POSE":
            selectedBones = bpy.context.selected_pose_bones
            if len(selectedBones) != 2:
                row.label(text="Select two bones!")
            if selectedBones:
                targetBone = selectedBones[0]
                if len(selectedBones) == 2:
                    twistBone = selectedBones[1]

                    row = layout.row()
                    row.label(text="Target Bone: " + targetBone.name)
                    row = layout.row()
                    row.label(text="Twist Bone: " + twistBone.name)
                    
                    row = layout.row()
                    row.prop(bpy.context.scene.quicktwist, "twistrotation")
                    row = layout.row()
                    row.prop(bpy.context.scene.quicktwist, "targetrotation")
                    row = layout.row()
                    row.prop(bpy.context.scene.quicktwist, "influence")
                    row = layout.row()
                    row.operator(addQuickDriver.bl_idname, text=addQuickDriver.bl_label)
        else:
            row.label(text="You must be in Pose Mode!")
            
class driverPrefs(bpy.types.PropertyGroup):
    targetrotation: bpy.props.EnumProperty(
        name="Target Rotation",
        items=(('ROT_X','X','',0),
                ('ROT_Y','Y','',1),
                ('ROT_Z','Z','',2)),
        default='ROT_X',
        )
        
    twistrotation: bpy.props.EnumProperty(
        name="Twist Rotation",
        items=(("0",'X','',0),
                ('1','Y','',1),
                ('2','Z','',2)),
        default=0,
        )
        
    influence: bpy.props.FloatProperty(
        name="Influence",
        min=0.0,
        max=1.0,
        default=0.5,
        )

cls = (addQuickDriver,QuickTwistPanel,driverPrefs)

def register():
    for c in cls:
        bpy.utils.register_class(c)
    
    bpy.types.Scene.quicktwist = bpy.props.PointerProperty(type=driverPrefs)

if __name__ == "__main__":
    register()
