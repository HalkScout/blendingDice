import bpy

from dice.die import Die

class D6(Die):
    def __init__(self):
        Die.__init__(self, 'd6', scale=(50, 50, 5), offset=10)
        offset = self.offset
        self.numbers = [
            ('1_', (0, 0, -offset), (180, 0, 0)),
            ('2_', (-offset, 0, 0), (0, -90, 0)),
            ('3_', (0, offset, 0),  (90, -90, -180)),
            ('4_', (0, -offset, 0), (90, -90, 0)),
            ('5_', (offset, 0, 0),  (0, 90, 0)),
            ('6_', (0, 0, offset),  (0, 0, 0))
        ]

    def create_mesh(self, collection):
        verts = ((-10.0, -10.0, -10.0),
            (-10.0, -10.0, 10.0),
            (-10.0, 10.0, -10.0),
            (-10.0, 10.0, 10.0),
            (10.0, -10.0, -10.0),
            (10.0, -10.0, 10.0),
            (10.0, 10.0, -10.0),
            (10.0, 10.0, 10.0))
        faces = ((0, 1, 3, 2),
            (2, 3, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (2, 6, 4, 0),
            (7, 3, 1, 5))
        me = bpy.data.meshes.new("mesh."  + self.name)
        me.from_pydata(verts, [], faces)
        obj = bpy.data.objects.new(self.name, me)
        collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        return obj