import os
filename = os.path.join(os.path.dirname(bpy.data.filepath), "bdr5mov.py")
exec(compile(open(filename).read(), filename, 'exec'))