filename = os.path.join(os.path.dirname(bpy.data.filepath), "bdr1mov.py")
exec(compile(open(filename).read(), filename, 'exec'))