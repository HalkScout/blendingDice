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
def create(mesh_name="{mesh.name}", obj_name="{obj.name}"):
    context = bpy.context
    verts = ({verts})
    faces = ({faces})
    me = bpy.data.meshes.new(mesh_name)
    me.from_pydata(verts, [], faces)
    ob = bpy.data.objects.new(obj_name, me)
    context.collection.objects.link(ob)
    context.view_layer.objects.active = ob""")
txt.close()