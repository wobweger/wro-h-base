
import bpy
import os

sDN='/wrk/dat/tmp/toEncode/20231024/'
iFrmStart=0
for sFN in os.listdir(sDN+'/04'):
    sTmpDN=sDN+'/04'
    sTmpFN=os.path.join(sDN+'04',sFN)
    print(sTmpFN)
    oMov=bpy.context.scene.sequence_editor.sequences.new_movie('test01',filepath=sDN+'/'+sFN,channel=4,frame_start=iFrmStart)
    iFrmStart=oMov.frame_final_end
