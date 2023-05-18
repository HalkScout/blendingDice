import bpy

from dice.die import Die

class D8(Die):
    def __init__(self):
        Die.__init__(self, 'd8', scale=(50, 50, 5), offset=10)
        offset = self.offset
        self.numbers = [
            ('1_', (0, 0, offset),          (0, 0, 0)),
            ('2_', (0, -offset, offset/4),  (108, 180, 0)),
            ('3_', (0, offset, 0),          (56.3, 239, -180)),
            ('4_', (0, -offset, 0),         (90, -90, 0)),
            ('5_', (offset, 0, 0),          (0, 90, 0)),
            ('6_', (offset/2, 0, offset/2),          (0, 0, 0)),
            ('7_', (0, offset, -offset/6),          (-71.5, 180, 0)),
            ('8_', (0, 0, -offset),         (180, 0, 0))
        ]

    def create_mesh(self, collection):
        verts = ((10.0, 6.683025360107422, -9.99974536895752),
            (-10.0, -6.683021545410156, 9.999747276306152),
            (0.0, 13.365745544433594, 9.99997329711914),
            (0.0, -13.365745544433594, -9.999971389770508),
            (10.0, -6.683021545410156, 9.999747276306152),
            (-10.0, 6.683025360107422, -9.99974536895752))
        faces = ((4, 0, 2),
            (4, 2, 1),
            (4, 1, 3),
            (4, 3, 0),
            (5, 2, 0),
            (5, 1, 2),
            (5, 3, 1),
            (5, 0, 3))
        me = bpy.data.meshes.new('mesh.' + self.name)
        me.from_pydata(verts, [], faces)
        obj = bpy.data.objects.new(self.name, me)
        collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        return obj