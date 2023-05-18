import bpy

import math
from mathutils import Euler

def select(name):
    obj = bpy.data.objects[name]
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    return obj

def deselect_all():
    for obj in bpy.context.selected_objects:
        obj.select_set(False)

def create_text_obj(txt: str, offset: tuple, rotation: tuple, scale: tuple, collection):
    # Deselect all
    deselect_all()
    # Select object
    obj = select(txt)
    # Duplicate number
    new_obj = obj.copy()
    new_obj.data = obj.data.copy()
    collection.objects.link(new_obj)
    # Warp duplicated number
    location = tuple(map(sum, zip((0, 0, 0), offset)))
    rotation_euler = tuple(map(math.radians, rotation))
    new_obj.location = location
    new_obj.rotation_euler = Euler(rotation_euler, 'XYZ')
    new_obj.scale = scale
    return new_obj

def apply_bool_modifier(txt: str, dice_obj, text_obj):
    modifier = dice_obj.modifiers.new(type="BOOLEAN", name='bool_' + txt)
    modifier.object = text_obj
    modifier.operation = 'DIFFERENCE'
    bpy.ops.object.modifier_apply(modifier=modifier.name)

def create_numbers(dice_obj, collection, scale, numbers):
    for num in numbers:
        txt, loc_offset, rotation = num
        txt_obj = create_text_obj(txt, loc_offset, rotation, scale, collection)
        #apply_bool_modifier(txt, dice_obj, txt_obj)