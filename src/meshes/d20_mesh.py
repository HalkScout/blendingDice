import bpy

def create(mesh_name="mesh.d20.001", obj_name="d20"):
    context = bpy.context
    verts = ((11.079300880432129, 6.396636962890625, 2.4432802200317383),
        (-11.079300880432129, 6.396636962890625, 2.4432802200317383),
        (11.079300880432129, -6.396636962890625, -2.4432802200317383),
        (-11.079300880432129, -6.396636962890625, -2.4432802200317383),
        (6.847384452819824, -3.95330810546875, 10.349987030029297),
        (6.847384452819824, 3.95330810546875, -10.349987030029297),
        (-6.847384452819824, -3.95330810546875, 10.349987030029297),
        (-6.847384452819824, 3.95330810546875, -10.349987030029297),
        (8.98817233974114e-08, 7.906707763671875, 10.349954605102539),
        (8.98817233974114e-08, -12.79327392578125, 2.443333625793457),
        (8.98817233974114e-08, 12.79327392578125, -2.443333625793457),
        (8.98817233974114e-08, -7.906707763671875, -10.349954605102539))
    faces = ((0, 8, 4),
        (0, 5, 10),
        (2, 4, 9),
        (2, 11, 5),
        (1, 6, 8),
        (1, 10, 7),
        (3, 9, 6),
        (3, 7, 11),
        (0, 10, 8),
        (1, 8, 10),
        (2, 9, 11),
        (3, 11, 9),
        (4, 2, 0),
        (5, 0, 2),
        (6, 1, 3),
        (7, 3, 1),
        (8, 6, 4),
        (9, 4, 6),
        (10, 5, 7),
        (11, 7, 5))
    me = bpy.data.meshes.new(mesh_name)
    me.from_pydata(verts, [], faces)
    ob = bpy.data.objects.new(obj_name, me)
    context.collection.objects.link(ob)
    context.view_layer.objects.active = ob