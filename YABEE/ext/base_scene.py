import bpy, os

order = 1
target = 'scene'
enabled = True

def invoke(all_data, target_data, context, fname, flags=None):
    from ..yabee_libs.egg_writer import write_out
    # todo this is unnecessary. flat is better than nested
    # have to change the loader though
    target_data['paths'] = {'sounds': 'res',
                            'meshes': 'res',
                            'images': 'res',
                            'materials': 'res'
                            }
    target_data['comment'] = 'Export from Blender ' + bpy.app.version_string
    target_data['b_version'] = bpy.app.version

    if context.scene.world:
        target_data['ambient_color'] = list(context.scene.world.ambient_color)
        target_data['horizon_color'] = list(context.scene.world.horizon_color)

    sfname = os.path.split(fname)[-1]
    sfname = os.path.splitext(sfname)[0]
    # sfname = os.path.join(target_data['paths']['meshes'],
    #                      sfname)
    target_data['scene_mesh'] = sfname

    objects = [obj.name for obj in context.scene.objects if obj.type == 'MESH']
    path = os.path.join(os.path.dirname(fname), target_data['paths']['meshes'], sfname + '.egg')
    # todo use the settings
    write_out(path, {}, 0, 0, 0, 0, 1, 'tex', 'BLENDER', 'RAW', {}, 0, 1, 0, objects, 0, 0)

    return target_data
