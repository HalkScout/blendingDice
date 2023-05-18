import bpy

def create(mesh_name="mesh.d8.001", obj_name="d8"):
    context = bpy.context
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
    me = bpy.data.meshes.new(mesh_name)
    me.from_pydata(verts, [], faces)
    ob = bpy.data.objects.new(obj_name, me)
    context.collection.objects.link(ob)
    context.view_layer.objects.active = ob