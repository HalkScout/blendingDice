import bpy

from dice.die import Die

class D10(Die):
    def __init__(self):
        Die.__init__(self, 'd10', scale=(50, 50, 5), offset=10)
        offset = self.offset
        self.numbers = [
            ('1_', (0, 0, offset), (0, 0, 0)),
            ('2_', (0, -offset/1.125, offset/3), (108, 180, 0)),
            ('3_', (-offset/1.5, -offset/2, -offset/3), (60, 125, -90)),
            ('4_', (-offset/1.5, offset/2, offset/3), (60, -55, -90)),
            ('5_', (offset/1.5, -offset/2, -offset/3), (240, -55, -90)),
            ('6_', (offset/1.5, offset/2, offset/3), (60, 55, 90)),
            ('7_', (0, offset/1.125, -offset/3), (108, 0, 180)),
            ('8_', (0, 0, -offset), (180, 0, 0))
            ('9_', (0, 0, -offset), (180, 0, 0))
            ('10_', (0, 0, -offset), (180, 0, 0))
        ]

    def create_mesh(self, collection):
        verts = ((2.3841858265427618e-08, 11.818984985351562, 9.991494178771973),
            (2.3841858265427618e-08, -11.818984985351562, -9.991494178771973),
            (11.00469970703125, 3.3342971801757812, -2.361299991607666),
            (6.801278114318848, 4.2148590087890625, -9.99837589263916),
            (2.3841858265427618e-08, 7.999931335449219, -10.0),
            (6.801278114318848, -4.2148590087890625, 9.99837589263916),
            (11.00469970703125, -3.3342971801757812, 2.361300468444824),
            (-6.801278114318848, -4.2148590087890625, 9.99837589263916),
            (2.3841858265427618e-08, -7.999931335449219, 10.0),
            (-11.00469970703125, -3.3342971801757812, 2.361300468444824),
            (-11.00469970703125, 3.3342971801757812, -2.361299991607666),
            (-6.801278114318848, 4.2148590087890625, -9.99837589263916))
        faces = ((0, 2, 3, 4),
            (5, 6, 2, 0),
            (5, 0, 7, 8),
            (7, 0, 10, 9),
            (4, 11, 10, 0),
            (8, 1, 6, 5),
            (6, 1, 3, 2),
            (3, 1, 11, 4),
            (9, 10, 11, 1),
            (1, 8, 7, 9))
        me = bpy.data.meshes.new('mesh.' + self.name)
        me.from_pydata(verts, [], faces)
        obj = bpy.data.objects.new(self.name, me)
        collection.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        return obj