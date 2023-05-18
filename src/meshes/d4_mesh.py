import bpy

def create(mesh_name="mesh.d4.001", obj_name="d4"):
    context = bpy.context
    verts = ((-1.5497207641601562e-06, 0.0, -15.0),
        (-12.247448921203613, -7.071067810058594, 5.000001430511475),
        (3.5762786865234375e-07, 14.142135620117188, 5.000000476837158),
        (12.24744987487793, -7.071063995361328, 4.999999523162842))
    faces = ((0, 1, 2),
        (0, 2, 3),
        (0, 3, 1),
        (1, 3, 2))
    me = bpy.data.meshes.new(mesh_name)
    me.from_pydata(verts, [], faces)
    ob = bpy.data.objects.new(obj_name, me)
    context.collection.objects.link(ob)
    context.view_layer.objects.active = ob