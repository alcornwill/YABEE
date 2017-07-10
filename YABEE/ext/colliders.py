
order = 1
target = 'object'  # this literally means nothing right?

import bpy

def invoke(data, fname, flags=None):
    for obj in bpy.context.selected_objects:
        if obj.game.use_collision_bounds:
            collider = {}
            collider["type"] = obj.game.collision_bounds_type
            collider["bounds"] = list(obj.dimensions)
            # NOTE: blender doesn't let you have no collision group/mask, so group 16 reserved for 'allOff'
            collider["from"] = list(obj.game.collision_group)[:-1]
            collider["into"] = list(obj.game.collision_mask)[:-1]
            # todo use groups for compound colliders?
            data["colliders"][obj.name] = collider
