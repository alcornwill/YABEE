
order = 1
target = 'object'  # this literally means nothing right?

import bpy

def invoke(data, fname, flags=None):
    for obj in bpy.context.selected_objects:
        if obj.game.use_collision_bounds:
            collider = {}
            collider["type"] = obj.game.collision_bounds_type
            collider["bounds"] = list(obj.dimensions)
            # note: for cube parameters are bounds / 2
            collider["mask"] = list(obj.game.collision_mask)
            # todo use groups for compound colliders?
            data["colliders"][obj.name] = collider