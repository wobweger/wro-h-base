#----------------------------------------------------------------------------
# Name:         bthvn00.py
# Purpose:      uses tesseract OCR to process single file
#               or performs batch file process on folder (recursively)
#               openCV or integrated image reader (suffix Raw) can be utilized
#               str or xml outputs are supported
#
#               used lindworm additional basic framework for 
#               easy command line argument parsing, logging
#               
# Setup:
#               pip install pytesseract
#               pip install tesseract
#               pip install opencv-python
#               pip install lindworm
#
# Author:       Walter Obweger
#
# Created:      20210716
# CVS-ID:       $Id$
# Copyright:    (c) 2021 by Walter Obweger
# Licence:      MIT license
#----------------------------------------------------------------------------

import sys
import os
import fnmatch
from optparse import OptionParser
import platform
import traceback
import logging
import logging.handlers

import os
import os.path

import cv2

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import lindworm
from lindworm.ldmArg import ldmArg
from lindworm.logUtil import ldmUtilLog

__version__='0.0.1'

def ocr(sInFN,
            sOtFN=None,
            sKind=None,
            oLog=None,
            iShow=0,
            iVerbose=1):
    try:
        # +++++ beg:init
        iRet=0
        bLog=0
        if oLog is not None:
            bLog=1
        # ----- end:init
        # +++++ beg:use openCV
        cKey=0
        iUseCV=0
        if sKind is None:
            iUseCV=1
        elif sKind.endswith('Raw'):
            iUseCV=0
        else:
            iUseCV=1
        if iUseCV>0:
            oLog.logInf('ocr:beg sOnFN:%r sOtFN:%r',sInFN,sOtFN)
            img_cv = cv2.imread(sInFN)
            img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            if iShow>1:
                # +++++ beg:
                sTitle="org:%r"%(sInFN)
                cv2.imshow(sTitle, img_cv)
                sTitle="rgb:%r"%(sInFN)
                cv2.imshow(sTitle, img_rgb)
                cKey=cv2.waitKey(0)
                #cv2.destroyAllWindows()
                #print("cKey:%r"%(cKey))
                #print("cKey:%r %d"%(cKey,ord(cKey[0])))
                # ----- end:
            elif iShow>0:
                # +++++ beg:
                sTitle="rgb:%r"%(sInFN)
                cv2.imshow(sTitle, img_rgb)
                cKey=cv2.waitKey(0)
                #cv2.destroyAllWindows()
                # ----- end:
        # ----- end:use openCV
        # +++++ beg:optical character recognition
        iOutBin=0
        if (sKind is None) or (sKind=='str'):
            sOcr=pytesseract.image_to_string(img_rgb)
            sExt='.txt'
        elif sKind=='xml':
            sOcr=pytesseract.image_to_alto_xml(img_rgb)
            sExt='.xml'
            iOutBin=1
        elif sKind=='strRaw':
            sOcr=pytesseract.image_to_string(sInFN)
            sExt='.txt'
        elif sKind=='xmlRaw':
            sOcr=pytesseract.image_to_alto_xml(sInFN)
            sExt='.xml'
            iOutBin=1
        else:
            sOcr=pytesseract.image_to_string(img_rgb)
            sExt='.txt'
        # ----- end:optical character recognition
        # +++++ beg:output
        if sOtFN is not None:
            # +++++ beg:create output directories
            try:
                sTmpDN,sTmpFN=os.path.split(sOtFN)
                os.makedirs(sTmpDN)
            except:
                pass
            # ----- end:create output directories
            # +++++ beg:determine file mode
            if iOutBin==0:
                sMode='w'
            else:
                sMode='w+b'
            # ----- end:determine file mode
            # +++++ beg:write to file
            with open(sOtFN+sExt, sMode) as f:
                f.write(sOcr)
                if iVerbose>0:
                    print('wrote to sOtFN:%r'%(sOtFN+sExt))
            # ----- end:write to file
        # ----- end:output
        iRet=1
        # +++++ beg:close CV windows
        if iUseCV>0:
            if iShow>0:
                # +++++ beg:
                #cKey=cv2.waitKey(0)
                cv2.destroyAllWindows()
                if iVerbose>5:
                    print("cKey:%r"%(cKey))
                if cKey==27:    # ESC pressed
                    iRet=11
                # ----- end:
        # ----- end:close CV windows
    except:
        if oLog is not None:
            oLog.logTB()
        iRet=-1
    oLog.logInf('ocr:end sOnFN:%r sOtFN:%r iRet:%d',sInFN,sOtFN,iRet)
    return iRet


def execMain(sOutDN          ='./out',
            sImgDN          ='.',
            sImgFN          =None,
            sKind           =None,
            iShow           =0,
            iVerbose        =10):
    # +++++ beg:
    # ----- end:
    
    # +++++ beg:init
    iRet=0
    oLog=ldmUtilLog('ocr')
    oLog.logInf('sImgDN:%r',sImgDN)
    oLog.logInf('sOutDN:%r',sOutDN)
    oLog.logInf('sKind:%r',sKind)
    # ----- end:init
    try:
        # +++++ beg:single or batch processing
        if sImgFN is not None:
            ocr(sImgFN,'BeethovenComplete01.txt',oLog=oLog)
            iRet+=1
        else:
            # +++++ beg:prepare batch processing
            lExt=['png','jpg','jpeg','JPG']
            iLenImgDN=len(sImgDN)
            oLog.logDbg('execMain:sImgDN:%r iLenImgDN:%d',sImgDN,iLenImgDN)
            # ----- end:prepare batch processing
            # +++++ beg:walk through directories
            for sRoot,lDN,lFN in os.walk(sImgDN):
                # +++++ beg:handle directory
                sRelDN=sRoot[iLenImgDN+1:]
                oLog.logInf('execMain:sRelDN:%r',sRelDN)
                oLog.logDbg('    sRoot:%r',sRoot)
                # ----- end:handle directory
                # +++++ beg:loop over files
                for sFN in lFN:
                    # +++++ beg:handle files
                    iPosExt=sFN.rfind('.')
                    if iPosExt>0:
                        # +++++ beg:check extension, valid image file
                        sExt=sFN[iPosExt+1:]
                        if sExt in lExt:
                            # +++++ beg:generate output filename
                            sTmpFN=os.path.join(sRoot,sFN)
                            sOutFN=os.path.join(sOutDN,sRelDN,sFN[:iPosExt])
                            oLog.logDbg('    sOutDN:%r sRelDN:%r',sOutDN,sRelDN)
                            oLog.logDbg('    sTmpFN:%r sOutFN:%r',sTmpFN,sOutFN)
                            # ----- end:generate output filename
                            # +++++ beg:perform ocr
                            iR=ocr(sTmpFN,
                                    sOtFN=sOutFN,
                                    sKind=sKind,
                                    oLog=oLog,
                                    iShow=iShow,
                                    iVerbose=iVerbose)
                            if iR==11:  # ESC pressed on image show
                                iShow=0
                            # ----- end:perform ocr
                            iRet+=1
                        # ----- end:check extension, valid image file
                    # ----- end:handle files
                # ----- end:loop over files
            # ----- end:walk through directories
        # ----- end:single or batch processing
        if iVerbose>0:
            print('converted ',iRet,'files')
        oLog.logInf('converted %d files',iRet)
    except:
        oLog.logTB()
        iRet=-1
    return iRet

def main(args=None):
    # +++++ beg:
    # ----- end:
    
    # +++++ beg:init
    iRet=0
    # ----- end:init
    # +++++ beg:setup command line parser
    usage = "usage: %prog [options]"
    oArg=ldmArg(sUsage=usage,sVer=__version__,iVerbose=0)
    oArg.addOpt('sOutDN',
            sDft='./out',
            sHlp='output directory',
            sMeta='output directory',
            )
    oArg.addOpt('sImgDN',
            sDft='./img',
            sHlp='image folder',
            sMeta='./folder/to/visit')
    oArg.addOpt('sImgFN',
            sDft=None,
            sHlp='image source',
            sMeta='./img.png')
    oArg.addOpt('sKind',
            sDft='str',
            sHlp='conversion output format',
            sMeta='str|xml|str|xmlRaw')
    oArg.addOpt('iShow',
            sDft=0,
            sHlp='show images',
            sMeta='0|1')
    oArg.addOpt('sTesserActDN',
            sDft='c:/apps/tesseractOCR/tesseract.exe',
            sHlp='tesserAct OCR installation path',
            sMeta='/path/to/tesserAct-OCR')
    
    oArg.addOpt('sLogFN',
            sDft='./log/bthvn00.log',
            sHlp='log filename',
            sVerbose='log file',
            sMeta='../path/to/bthvn.log')
    # ----- end:setup command line parser
    # +++++ beg:parse command line
    iRet=oArg.prcParse(args)
    sLogFN=getattr(oArg,"sLogFN",None)
    if oArg.GetVerbose(10):
        print('ldmArg.prcParse:%d'%(iRet))
        print(" log FN:     %r"%(sLogFN))
    # ----- end:parse command line
    # +++++ beg:prepare logging
    if sLogFN is not None:
        import lindworm.logUtil as logUtil
        logUtil.logInit(sLogFN,iLevel=logging.DEBUG)
    #else:
    #    return 0                            # 20200602 wro:help on arguments called
    oLog=ldmUtilLog('main')
    # ----- end:prepare logging
    # +++++ beg:setup pytesserAct tesserAct OCR installation path
    try:
        sPathTesserAct=getattr(oArg,"sTesserActDN")
        pytesseract.pytesseract.tesseract_cmd = sPathTesserAct
        if oArg.iVerbose>5:
            print(pytesseract.get_languages(config=''))
    except:
        oLog.logTB()
        sys.stderr.write('\nargument tesserActDN is required, aborting processing\n')
        sys.stderr.write('panic\n')
        return -1
    # +++++ beg:perform main
    # +++++ beg:perform main
    iCLI=getattr(oArg,"iCLI",1)
    if iCLI==0:
        # +++++ beg:perform GUI version
        oLog.logWrn('GUI not implemented yet')
        print('GUI not implemented yet')
        # ----- end:perform GUI version
    else:
        # +++++ beg:perform main action
        iR=execMain(
                sOutDN          =getattr(oArg,"sOutDN"),
                sImgDN          =getattr(oArg,"sImgDN"),
                sImgFN          =getattr(oArg,"sImgFN"),
                sKind           =getattr(oArg,"sKind"),
                iShow           =getattr(oArg,"iShow"),
                iVerbose        =oArg.iVerbose)
        if iR>0:
            iRet+=1
        else:
            iRet=iR
        # ----- end:perform main action
    # ----- end:perform main
    return iRet


if __name__ == "__main__":
    # +++++ beg:call entry point
    main(args=None)
    # ----- end:call entry point
