import bpy
import os
import pandas
import time
import shutil
import lindworm.logUtil as ldmLg
import lindworm.logUtil as logUtil
logUtil.logInit("./x_log/bdr7mov.log",iLevel=0,sLogger=None)

# define raw data root folder
sMovRootDN='/wrk/dat/tmp/toEncode'
# define day to process, sequence and source
sDay='20231015'
iMovKind=1
iSeqBeg=1

#iMovKind=1      # only wild life cameras, sSubDN length <4
#iMovKind=2      # only dig cameras, sSubDN length >8
#iMovKind=3      # all
iSeqLen=100



sMovBaseDN=os.path.join(sMovRootDN,sDay)
sPdsFN='./'+sDay[:6]+'/64l_0-'+sDay+'.xlsx'
ldmLg.logInf('sDay:%r sMovBaseDN:%r sPdsFN:%r cwd:%r',sDay,sMovBaseDN,sPdsFN,os.getcwd())

print(sPdsFN)
oWrk=pandas.ExcelFile(sPdsFN)
lSht=oWrk.sheet_names
print(lSht)
sSht=lSht[1]
oVid=oWrk.parse(sSht)
oVid.head(5)
oVid.sort_values(['lbl'],inplace=True)
print(oVid.shape)
ldmLg.logInf('sDay:%r sMovBaseDN:%r sPdsFN:%r shape:%r',sDay,sMovBaseDN,sPdsFN,oVid.shape)

def delProxy(sMovBaseDN):
    for sSubDN in os.listdir(sMovBaseDN):
        sProxyDN=sMovBaseDN+'/'+sSubDN+'/'+'BL_proxy'
        if os.path.exists(sProxyDN):
            ldmLg.logDbg('proxy exists %r',sProxyDN)
            shutil.rmtree(sProxyDN)

ldmLg.logInf('delProxy %r',sMovBaseDN)
delProxy(sMovBaseDN)

bpy.context.area.type = 'SEQUENCE_EDITOR'
scene = bpy.context.scene

iFrmStart=0
iOfs=-1

#iOfsBeg=301
#iOfsEnd=400

if iSeqBeg>0:
    iOfsBeg=(iSeqBeg*iSeqLen)+1
else:
    iOfsBeg=0
iOfsEnd=(iSeqBeg+1)*iSeqLen
ldmLg.logInf('sPdsFN:%r iSeqBeg:%d iSeqLen:%d iOfsBeg:%d iOfsEnd:%d',sPdsFN,iSeqBeg,iSeqLen,iOfsBeg,iOfsEnd)

for sIdx in oVid.index:
    iOfs+=1
    if iOfs>iOfsEnd:
        break
    if iOfs<iOfsBeg:
        oMov = scene.sequence_editor.active_strip
        iFrmStart=oMov.frame_final_end#+100
        continue

    print(sIdx)
    oVidMov=oVid.loc[sIdx]
    sLbl=oVidMov['lbl']
    print(sIdx,sLbl)
    ldmLg.logDbg('sIdx %r sLbl:%r',sIdx,sLbl)
    sMovDN=oVidMov['DN']
    sMovFN=oVidMov['FN']
    ldmLg.logDbg('sMovDN %r sMovFN:%r',sMovDN,sMovFN)
    
    sPosDN=sMovDN.find('/.')
    sRelDN=sMovDN[sPosDN+2:]
    print(sRelDN)
    ldmLg.logDbg('sRelDN %r',sRelDN)

    if iMovKind==1:
        if len(sRelDN)>4:
            continue
    elif iMovKind==2:
        if len(sRelDN)<8:
            continue
    ldmLg.logDbg('iOfs:%d sMovBaseDN %r sRelDN %r,sMovFN:%r',iOfs,sMovBaseDN,sRelDN,sMovFN)
    sTmpFN=os.path.join(sMovBaseDN+sRelDN,sMovFN)
    print('%4d'%iOfs,sTmpFN)
    ldmLg.logDbg('iOfs:%d sTmpFN:%r',iOfs,sTmpFN)
    try:
        dRes=bpy.ops.sequencer.movie_strip_add(filepath=sTmpFN,frame_start=iFrmStart,channel=3,
                                        #replace_sel=True,fit_method='ORIGINAL',
                                        sound=True)#,use_framerate=True)
                                        #sound=False)#,use_framerate=True)
        print(dRes)
        ldmLg.logDbg('sRelDN:%r sTmpFN:%r dRes:%r',sRelDN,sTmpFN,dRes)
        #bpy.ops.sequencer.movie_strip_add(sTmpDN)
        #iFrmStart=oMov.frame_final_end
        oMov = scene.sequence_editor.active_strip
        ldmLg.logDbg('name:%r',oMov.name)
        if oMov.name.startswith(sTmpFN):
            pass
        else:
            #continue
            pass
        oMov.use_proxy=False
        iFrmStartNxt=oMov.frame_final_end#+100
    except:
        ldmLg.logTB()
        iFrmStartNxt=iFrmStart+910
    try:
        dRes=bpy.ops.sequencer.effect_strip_add(type='TEXT',frame_start=iFrmStart,channel=5)
        oTxt = scene.sequence_editor.active_strip
        oTxt.name=sRelDN[1:]+'_'+sMovFN
        oTxt.frame_final_duration=90
        oTxt.location=(0.01,0.99)
        oTxt.text=sRelDN[1:]+':'+sLbl
        oTxt.align_x='LEFT'
        oTxt.align_y='TOP'
        oTxt.use_box=True
        oTxt.font_size=36
        oTxt.wrap_width=0.35
    except:
        ldmLg.logTB()
        pass
    ldmLg.logDbg('iFrmStart :%d Nxt:%d',iFrmStart,iFrmStartNxt)
    iFrmStart=iFrmStartNxt
    #time.sleep(0.5)
ldmLg.logInf('delProxy %r again',sMovBaseDN)
delProxy(sMovBaseDN)
