import os
filename = os.path.join(os.path.dirname(bpy.data.filepath), "bdr6mov.py")
exec(compile(open(filename).read(), filename, 'exec'))