import bpy
import os

bpy.context.area.type = 'SEQUENCE_EDITOR'
scene = bpy.context.scene
sDN='/wrk/dat/tmp/toEncode/20231024'
iFrmStart=0
iOfs=0
for sTmpDN in os.listdir(sDN):
    if len(sTmpDN)>3:
        continue
    for sFN in os.listdir(sDN+'/'+sTmpDN):
        tExt=os.path.splitext(sFN)
        if len(tExt)<2:
            continue
        sExt=tExt[1]
        if sExt in ['.AVI','.avi','.MOV','.mov']:
            pass 
        else:
            print('skip',sTmpFN)
            continue
        sTmpFN=os.path.join(sDN+'/'+sTmpDN,sFN)
        print('%4d'%iOfs,sTmpFN)
        dRes=bpy.ops.sequencer.movie_strip_add(filepath=sTmpFN,frame_start=iFrmStart,channel=4)
        #bpy.ops.sequencer.movie_strip_add(sTmpDN)
        #iFrmStart=oMov.frame_final_end
        oMov = scene.sequence_editor.active_strip
        iFrmStart=oMov.frame_final_end
        iOfs+=1
        #iFrmStart=iOfs*1000
        #if iOfs>2:
        #    break
