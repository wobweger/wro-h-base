import bpy
import os

bpy.context.area.type = 'SEQUENCE_EDITOR'
sDN='/wrk/dat/tmp/toEncode/20231024/'
for sFN in os.listdir(sDN+'/04'):
    sTmpDN=sDN+'/04'
    sTmpFN=os.path.join(sDN+'04',sFN)
    print(sTmpFN)
    bpy.ops.sequencer.movie_strip_add(filepath=sTmpFN)
    #bpy.ops.sequencer.movie_strip_add(sTmpDN)
