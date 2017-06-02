
order = 100
target = 'material'

def invoke(data, fname, flags=None):
    for material in bpy.data.materials:
        target_data = {} if material.name not in data['materials'] else data['materials'][material.name]
        target_data['use_physics'] = material.game_settings.physics
        if material.game_settings.physics:
            target_data['phys_friction'] = material.physics.friction
            target_data['phys_elasticity'] = material.physics.elasticity
