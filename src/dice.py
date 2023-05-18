if "bpy" not in locals():
    import bpy
    import sys
    import os

    dir = os.path.dirname(bpy.data.filepath)
    if not dir in sys.path:
        sys.path.append(dir)

import bpy
import dice.die
import dice.d6
import dice.d8
import util.text_utils

from importlib import reload
reload(dice.die)
reload(dice.d6)
reload(dice.d8)
reload(util.text_utils)

from dice.d6 import D6
from dice.d8 import D8
from meshes import (
    d4_mesh,
    d6_mesh,
    d8_mesh,
    d10_mesh,
    d12_mesh,
    d20_mesh
)

def create_dice(type, scale, offset):
    collection = bpy.data.collections.new(type)
    bpy.context.scene.collection.children.link(collection)
    match type:
        case 'd4':
            obj = d4_mesh.create(collection, type)
        case 'd6':
            D6().create()
        case 'd8':
            D8().create()
        case 'd10':
            obj = d10_mesh.create(collection, type)
        case 'd10_percentile':
            obj = d10_mesh.create(collection, type)
        case 'd12':
            obj = d12_mesh.create(collection, type)
        case 'd20':
            obj = d20_mesh.create(collection, type)
        
#create_dice('d4', scale=(50, 50, 5), offset=10)
#create_dice('d6', scale=(50, 50, 5), offset=10)
create_dice('d8', scale=(50, 50, 5), offset=10)
#create_dice('d10', scale=(50, 50, 5), offset=10)
#create_dice('d10_percentile', scale=(50, 50, 5), offset=10)
#create_dice('d12', scale=(50, 50, 5), offset=10)
#create_dice('d20', scale=(50, 50, 5), offset=10)