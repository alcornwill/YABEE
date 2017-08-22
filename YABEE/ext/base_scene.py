import bpy, os

order = 1
target = 'scene'

def invoke(data, fname, flags=None):
    target_data = data['scene']
    from ..yabee_libs.egg_writer import write_out
    target_data['comment'] = 'Export from Blender ' + bpy.app.version_string

    world = bpy.context.scene.world
    if world:
        if world.light_settings.use_environment_light:
            env = world.light_settings.environment_energy
            target_data['ambient_color'] = (env, env, env)
            # target_data['ambient_color'] = list(bpy.context.scene.world.ambient_color)
        target_data['horizon_color'] = list(world.horizon_color)
        if world.mist_settings.use_mist:
            target_data['use_mist'] = True
            target_data['mist_falloff'] = world.mist_settings.falloff
            target_data['mist_start'] = world.mist_settings.start
            target_data['mist_depth'] = world.mist_settings.depth

    return target_data
