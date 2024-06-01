import bpy
import lindworm.logUtil as ldmLg
import lindworm.logUtil as logUtil
logUtil.logInit("./x_log/bdr7mov.log",iLevel=0,sLogger=None)

sScene = bpy.context.scene.name

### get all strips in the scene ###
lStrip = bpy.data.scenes[sScene].sequence_editor.sequences_all

dStripFrmBeg={}
for oMov in lStrip:
    iFrmBeg=oMov.frame_start
    if iFrmBeg in dStripFrmBeg:
        lMov=dStripFrmBeg[iFrmBeg]
    else:
        lMov=[]
        dStripFrmBeg[iFrmBeg]=lMov 
    lMov.append(oMov)


lKeys=list(dStripFrmBeg.keys())
lKeys.sort()

oMovPrv=None
iFrmEndPrv=0
for iFrmBeg in lKeys:
    ldmLg.logDbg('iFrmBeg:%d',iFrmBeg)
    oMovAct=None
    lMovAct=dStripFrmBeg[iFrmBeg]
    iFrmEnd=0
    for oMov in lMovAct:
        oMov.frame_start=iFrmEndPrv
        iFrmEndTmp=oMov.frame_start+oMov.frame_final_duration
        ldmLg.logDbg('iFrmBeg:%d iFrmEndTmp:%d oMov name:%r beg:%d dur:%d',
                            iFrmBeg,iFrmEndTmp,oMov.name,oMov.frame_start,oMov.frame_final_duration)
        if iFrmEndTmp>iFrmEnd:
            iFrmEnd=iFrmEndTmp
            oMovAct=oMov
    oMovPrv=oMovAct
    iFrmEndPrv=iFrmEnd
