import bpy, os

order = 1
target = 'scene'

def invoke(data, fname, flags=None):
    target_data = data['scene']
    from ..yabee_libs.egg_writer import write_out
    target_data['comment'] = 'Export from Blender ' + bpy.app.version_string

    if bpy.context.scene.world:
        target_data['ambient_color'] = list(bpy.context.scene.world.ambient_color)
        target_data['horizon_color'] = list(bpy.context.scene.world.horizon_color)

    return target_data
