import bpy

def create(collection, type="d4"):
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
    me = bpy.data.meshes.new("mesh."  + type)
    me.from_pydata(verts, [], faces)
    obj = bpy.data.objects.new(type, me)
    collection.objects.link(obj)
    context.view_layer.objects.active = obj
    return obj