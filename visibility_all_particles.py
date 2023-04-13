# Quickly changes visibility of objects with several particle systems for the current active object.

#  True = Show all particle systems. False = Hide all particle systems.
visible = True

import bpy
obj = bpy.context.active_object

if obj:
    for particle in obj.modifiers:
        if "ParticleSystem" in particle.name:
            particle.show_viewport = visible
