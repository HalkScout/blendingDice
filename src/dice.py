if "bpy" not in locals():
    import bpy
    import sys
    import os

    dir = os.path.dirname(bpy.data.filepath)
    if not dir in sys.path:
        sys.path.append(dir)

import bpy
import dice.die
import dice.d4
import dice.d6
import dice.d8
import dice.d10
import dice.d12
import dice.d20
import util.text_utils

from importlib import reload
reload(dice.die)
reload(dice.d4)
reload(dice.d6)
reload(dice.d8)
reload(dice.d10)
reload(dice.d12)
reload(dice.d20)
reload(util.text_utils)

from dice.d4 import D4
from dice.d6 import D6
from dice.d8 import D8
from dice.d10 import D10
from dice.d12 import D12
from dice.d20 import D20

def create_dice(type):
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
            D10().create()
        case 'd10_percentile':
            D10().create()
        case 'd12':
            D12().create()
        case 'd20':
            D20().create()
        

#create_dice('d6', scale=(50, 50, 5), offset=10)
#create_dice('d8', scale=(50, 50, 5), offset=10)
create_dice('d10')

#create_dice('d4', scale=(50, 50, 5), offset=10)
#create_dice('d10_percentile', scale=(50, 50, 5), offset=10)
#create_dice('d12', scale=(50, 50, 5), offset=10)
#create_dice('d20', scale=(50, 50, 5), offset=10)