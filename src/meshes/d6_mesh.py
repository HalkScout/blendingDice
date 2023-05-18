import bpy

def create(mesh_name="mesh.d6.001", obj_name="d6"):
    context = bpy.context
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
    me = bpy.data.meshes.new(mesh_name)
    me.from_pydata(verts, [], faces)
    ob = bpy.data.objects.new(obj_name, me)
    context.collection.objects.link(ob)
    context.view_layer.objects.active = ob