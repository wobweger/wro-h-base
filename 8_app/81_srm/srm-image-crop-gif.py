#----------------------------------------------------------------------------
# Name:         srm-image-crop-gif.py
# Purpose:      uses streamlit, PIL and imageio to 
#               crop images
#               create gif from cropped images
#               
# Setup:
#               pip install streamlit
#               pip install streamlit-cropper
#               pip install opencv-python
#               pip install PIL
#               pip install imageio
#
# Author:       Walter Obweger
#
# Created:      20221016
# CVS-ID:       $Id$
# Copyright:    (c) 2022 by Walter Obweger
# Licence:      MIT license
#----------------------------------------------------------------------------
# based on example usage found at pypi
# https://pypi.org/project/streamlit-cropper/
# hints from stackoverflow
# https://stackoverflow.com/questions/61282938/imageio-individual-frame-rates

import os
import shutil
import imageio

import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image
st.set_option('deprecation.showfileUploaderEncoding', False)

iVerbose=0
sBaseDN=''
sInpDN='/wrk/dat/LinWildLife/raw'
sOutDN='/wrk/dat/LinWildLife/crop'
sGifDN='/wrk/dat/LinWildLife/gif'

# Upload an image and set some options for demo purposes
st.header("image crop git")
img_file = st.sidebar.file_uploader(label='Upload a file', type=['png', 'jpg'])
realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
aspect_dict = {
    "1:1": (1, 1),
    "16:9": (16, 9),
    "4:3": (4, 3),
    "2:3": (2, 3),
    "Free": None
}
aspect_ratio = aspect_dict[aspect_choice]


if img_file:
    sUpLdDN,sUpLdFN=os.path.split(img_file.name)
    img = Image.open(img_file)
    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_box = st_cropper(img, 
                            realtime_update=realtime_update, 
                            box_color=box_color,
                            return_type="box",
                            aspect_ratio=aspect_ratio)
    if iVerbose>5:
        st.write(sUpLdDN)
        st.write(sUpLdFN)
    if iVerbose>0:
        st.write(cropped_box)
    if st.button('bulk apply save to outDN'):
        st.write('outDN:%r'%(sOutDN))
        iCnt=0
        if iVerbose>10:
            st.write(sInpDN)
        tCrop=(cropped_box["left"],
                cropped_box["top"],
                cropped_box["left"]+cropped_box["width"],
                cropped_box["top"]+cropped_box["height"])
        for sRoot,lDN,lFN in os.walk(sInpDN):
            if iVerbose>10:
                st.write(sRoot)
            for sFN in lFN:
                if iVerbose>20:
                    st.write(sFN)
                if sFN.endswith('.png'):
                    sCurFN=os.path.join(sRoot,sFN)
                    sCrpFN=os.path.join(sOutDN,sFN)
                    oImgCur=Image.open(sCurFN)
                    oImpCrp=oImgCur.crop(tCrop)
                    oImpCrp.save(sCrpFN)
                    iCnt+=1
                pass
            break
        st.write('%d file cropped'%(iCnt))
    slrFileToKeep=st.slider("keep every x-th file",min_value=1,max_value=100,value=10,step=1)
    if st.button('thin out'):
        lDelFN=[]
        iMax=slrFileToKeep
        st.write("files to keep %r"%(iMax))
        for sRoot,lDN,lFN in os.walk(sOutDN):
            iCnt=0
            lFN.sort()
            for sFN in lFN:
                if iVerbose>20:
                    st.write(sFN)
                if sFN.endswith('.png'):
                    sCrpFN=os.path.join(sOutDN,sFN)
                    if iVerbose>20:
                        st.write("iCnt:%d iMax:%d sFN:%r"%(iCnt,iMax,sFN))
                    if iCnt<=iMax:
                        if iCnt>0:
                            lDelFN.append(sCrpFN)
                        else:
                            if iVerbose>10:
                                st.write('keeP %r'%(sCrpFN))
                    else:
                        iCnt=0
                        if iVerbose>10:
                            st.write('keep %r'%(sCrpFN))
                    iCnt+=1
            break 
        for sFN in lDelFN:
            os.remove(sFN)
        st.write('removed %d files'%(len(lDelFN)))
    lPart=sUpLdFN.split('_')
    sPfx='_'.join(lPart[:-1])
    txtGifDN=st.text_input("gif FN",value=sPfx)
    slrGifFPS=st.slider("frames per sec",min_value=1,max_value=100,value=30,step=1)
    if st.button("gif"):
        sPfx=txtGifDN
        iFPS=slrGifFPS
        if len(sPfx)>0:
            iCount=0
            for sRoot,lDN,lFN in os.walk(sOutDN):
                lImg=[]
                lFN.sort()
                for sFN in lFN:
                    sTmpFN=os.path.join(sRoot,sFN)
                    lImg.append(imageio.v2.imread(sTmpFN))
            sGifFN='%s_%02d.gif'%(sPfx,iFPS)
            sGifFullFN=os.path.join(sGifDN,sGifFN)
            imageio.mimsave(sGifFullFN,lImg,'GIF',fps=iFPS)
            iCount+=1
            st.write('gif created',sGifFullFN)
    if st.button("del raw"):
        for sRoot,lDN,lFN in os.walk(sInpDN):
            for sFN in lFN:
                sTmpFN=os.path.join(sRoot,sFN)
                os.remove(sTmpFN)
    if st.button("archive cropped"):
        st.write("copy %r"%(sOutDN))
        sYr=lPart[0][:4]
        sTmpDN='_'.join(lPart[:3])
        sDstDN='/'.join([sOutDN,'..',sYr,lPart[0],sTmpDN])
        st.write("to %r"%(sDstDN))
        try:
            os.makedirs(sDstDN)
        except:
            pass
        for sRoot,lDN,lFN in os.walk(sOutDN):
            for sFN in lFN:
                if sFN.endswith('.png'):
                    sTmpFN=os.path.join(sRoot,sFN)
                    sDstFN=os.path.join(sDstDN,sFN)
                    shutil.move(sTmpFN,sDstFN)

            
