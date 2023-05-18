import bpy

from meshes import (
    d4_mesh,
    d6_mesh,
    d8_mesh,
    d10_mesh,
    d12_mesh,
    d20_mesh
)

def create_dice(num_faces):
    match str(num_faces):
        case '4':
            d4_mesh.create()
        case '6':
            d6_mesh.create()
        case '8':
            d8_mesh.create()
        case '10':
            d10_mesh.create()
        case '10p':
            d10_mesh.create(obj_name="d10_percentile")
        case '12':
            d12_mesh.create()
        case '20':
            d20_mesh.create()
        
create_dice(4)
create_dice(6)
create_dice(8)
create_dice(10)
create_dice('10p')
create_dice(12)
create_dice(20)