import bpy

dRes=bpy.ops.sequencer.select_all(action='SELECT')
print(dRes=={'FINISHED'})
print('FINISHED' in dRes)


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


bpy.data.scenes[sScene].sequence_editor.sequences_all['DSCF0002-igel.AVI']

bpy.data.scenes[sScene].sequence_editor.sequences_all['DSCF0002-igel.AVI'].frame_start in dStripFrmBeg
dStripFrmBeg[bpy.data.scenes[sScene].sequence_editor.sequences_all['DSCF0002-igel.AVI'].frame_start]
lKeys=list(dStripFrmBeg.keys())
lKeys.sort()

oMovPrv=None
for iFrmBeg in lKeys:
    if oMovPrv is None:
        oMovAct=None
        lMovAct=dStripFrmBeg[iFrmBeg]
        iFrmEnd=0
        for oMov in lMovAct:
            iFrmEndTmp=oMov.frame_start+oMov.frame_final_duration
            if iFrmEndTmp>iFrmEnd:
                iFrmEnd=iFrmEndTmp
                oMovAct=oMov
        oMovPrv=oMovAct
    else:
        oMovAct=None
        lMovAct=dStripFrmBeg[iFrmBeg]
        iFrmEnd=0
        for oMov in lMovAct:
            oMov.frame_start=iFrmEnd
            iFrmEndTmp=oMov.frame_start+oMov.frame_final_duration
            if iFrmEndTmp>iFrmEnd:
                iFrmEnd=iFrmEndTmp
                oMovAct=oMov
        if oMovAct is not None:
            oMovPrv=oMovAct
