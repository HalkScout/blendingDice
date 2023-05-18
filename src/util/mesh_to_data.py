"""
Taken from: https://blender.stackexchange.com/a/136888
"""

import bpy

context = bpy.context
obj = context.object

mesh = obj.data
faces = str(",\n        ".join(f'{p.vertices[:]}' for p in mesh.polygons))
verts = str(",\n        ".join(f"{v.co[:]}"  for v in mesh.vertices))

txt = open(str(obj.name) + "_mesh.py", "w")
txt.write(f"""import bpy\n
def create(collection, obj_name="{obj.name}"):
    context = bpy.context
    verts = ({verts})
    faces = ({faces})
    me = bpy.data.meshes.new("mesh." + {obj.name})
    me.from_pydata(verts, [], faces)
    obj = bpy.data.objects.new(obj_name, me)
    collection.objects.link(obj)
    context.view_layer.objects.active = obj
    return obj""")
txt.close()