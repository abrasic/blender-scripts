# Quickly changes visibility of objects with several particle systems for the current active object.

import bpy
obj = bpy.context.active_object

if obj:
    for particle in obj.modifiers:
        if "ParticleSystem" in particle.name:
            particle.show_viewport = not particle.show_viewport
