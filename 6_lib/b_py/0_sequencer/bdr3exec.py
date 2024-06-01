filename = os.path.join(os.path.dirname(bpy.data.filepath), "bdr3mov.py")
exec(compile(open(filename).read(), filename, 'exec'))