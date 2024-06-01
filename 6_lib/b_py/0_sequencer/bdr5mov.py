import bpy
import os

#bpy.context.area.type = 'SEQUENCE_EDITOR'
sDN='/wrk/dat/tmp/toEncode/20231024/'
iFrmStart=0
iOfs=0
for sFN in os.listdir(sDN+'/04'):
    sTmpDN=sDN+'/04'
    sTmpFN=os.path.join(sDN+'04',sFN)
    print('%4d'%iOfs,sTmpFN)
    #oMov=bpy.ops.sequencer.movie_strip_add(filepath=sTmpFN,frame_start=iFrmStart,channel=4)
    oMov=bpy.context.scene.sequence_editor.sequences.new_movie(sTmpDN,sFN, iOfs, iFrmStart)
    #bpy.ops.sequencer.movie_strip_add(sTmpDN)
    iFrmStart=oMov.frame_final_end
    iOfs+=1
    if iOfs>2:
        break
