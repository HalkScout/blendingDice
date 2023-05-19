import bpy

from dice.die import Die

class D4(Die):
    def __init__(self):
        Die.__init__(self, 'd4', scale=(50, 50, 5), offset=10)
        offset = self.offset
        self.numbers = [
            ('1_', (0, 0, -offset), (180, 0, 0)),
            ('2_', (-offset, 0, 0), (0, -90, 0)),
            ('3_', (0, offset, 0),  (90, -90, -180)),
            ('4_', (0, -offset, 0), (90, -90, 0))
        ]

    def create_mesh(self, collection):
        verts = ((-1.5497207641601562e-06, 0.0, -15.0),
            (-12.247448921203613, -7.071067810058594, 5.000001430511475),
            (3.5762786865234375e-07, 14.142135620117188, 5.000000476837158),
            (12.24744987487793, -7.071063995361328, 4.999999523162842))
        faces = ((0, 1, 2),
            (0, 2, 3),
            (0, 3, 1),
            (1, 3, 2))
        me = bpy.data.meshes.new('mesh.' + self.name)
        me.from_pydata(verts, [], faces)
        obj = bpy.data.objects.new(self.name, me)
        collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        return obj