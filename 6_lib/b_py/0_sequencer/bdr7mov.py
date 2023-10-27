import bpy
import os
import pandas

sDN='/wrk/dat/tmp/toEncode/20231024'
sPdsFN='./202310/64l_0-20231025.xlsx'
print(sPdsFN)
oWrk=pandas.ExcelFile(sPdsFN)
lSht=oWrk.sheet_names
print(lSht)
sSht=lSht[1]
oVid=oWrk.parse(sSht)
oVid.head(5)
oVid.sort_values(['lbl'],inplace=True)
print(oVid.shape)

bpy.context.area.type = 'SEQUENCE_EDITOR'
scene = bpy.context.scene

iFrmStart=0
iOfs=0

for sIdx in oVid.index:
    print(sIdx)
    oVidMov=oVid.loc[sIdx]
    sLbl=oVidMov['lbl']
    print(sIdx,sLbl)
    sMovDN=oVidMov['DN']
    sMovFN=oVidMov['FN']
    
    sPosDN=sMovDN.find('/.')
    sRelDN=sMovDN[sPosDN+2:]
    print(sRelDN)


    sTmpFN=os.path.join(sMovDN,sMovFN)
    print('%4d'%iOfs,sTmpFN)
    dRes=bpy.ops.sequencer.movie_strip_add(filepath=sTmpFN,frame_start=iFrmStart,channel=4)
    dRes=bpy.ops.sequencer.effect_strip_add(type='TEXT',frame_start=iFrmStart,channel=5)
    #bpy.ops.sequencer.movie_strip_add(sTmpDN)
    #iFrmStart=oMov.frame_final_end
    oMov = scene.sequence_editor.active_strip
    iFrmStart=oMov.frame_final_end
    iOfs+=1
