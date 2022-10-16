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
st.header("Cropper Demo")
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
    if st.button('apply save to outDN'):
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
                for sFN in lFN:
                    sTmpFN=os.path.join(sRoot,sFN)
                    lImg.append(imageio.v2.imread(sTmpFN))
            sGifFN='%s_%02d.gif'%(sPfx,iFPS)
            sGifFullFN=os.path.join(sGifDN,sGifFN)
            imageio.mimsave(sGifFullFN,lImg,'GIF',fps=iFPS)
            iCount+=1
            st.write('gif created',sGifFullFN)
