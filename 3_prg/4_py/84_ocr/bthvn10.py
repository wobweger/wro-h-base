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

import eyed3

import lindworm
from lindworm.ldmArg import ldmArg
from lindworm.logUtil import ldmUtilLog

__version__='0.0.1'

def updMp3Tag(sMp3FN,
            sTrkFN=None,
            sOutFN=None,
            sKind=None,
            oLog=None,
            iShow=0,
            iVerbose=1):
    try:
        # +++++ beg:init
        iRet=0
        bLog=0
        bLogTagRd=0
        if oLog is not None:
            bLog=1
        if bLog>0:
            if iVerbose>=0:
                bLogTagRd=1
        # ----- end:init
        # +++++ beg:
        oMp3=eyed3.load(sMp3FN)
        if bLogTagRd>0:
            oLog.logDbg('artist:%r album:%r title:%r track num:%r'%(oMp3.tag.artist,
                        oMp3.tag.album,oMp3.tag.title,oMp3.tag.track_num,))
        # ----- end:
        # +++++ beg:
        # ----- end:
        # +++++ beg:
        # ----- end:
        # +++++ beg:output
        if sOutFN is not None:
            # +++++ beg:create output directories
            try:
                sTmpDN,sTmpFN=os.path.split(sOutFN)
                os.makedirs(sTmpDN)
            except:
                pass
            # ----- end:create output directories
            # +++++ beg:determine file mode
            # ----- end:determine file mode
            # +++++ beg:write to file
            # ----- end:write to file
        # ----- end:output
        iRet=1
        # +++++ beg:close CV windows
        # ----- end:close CV windows
    except:
        if oLog is not None:
            oLog.logTB()
        iRet=-1
    oLog.logInf('ocr:end sOnFN:%r sOtFN:%r iRet:%d',sMp3FN,sOutFN,iRet)
    return iRet


def execMain(sOutDN          ='./out',
            sMp3DN          ='.',
            sTrkDN          =None,
            sKind           =None,
            iShow           =0,
            iVerbose        =10):
    # +++++ beg:
    # ----- end:
    
    # +++++ beg:init
    iRet=0
    oLog=ldmUtilLog('ocr')
    oLog.logInf('sMp3DN:%r',sMp3DN)
    oLog.logInf('sTrkDN:%r',sTrkDN)
    oLog.logInf('sOutDN:%r',sOutDN)
    oLog.logInf('sKind:%r',sKind)
    # ----- end:init
    try:
        # +++++ beg:single or batch processing
        if sMp3DN is None:
            #ocr(sMp3FN,'BeethovenComplete01.txt',oLog=oLog)
            iRet=-10
        else:
            # +++++ beg:prepare batch processing
            lExt=['mp3',]
            iLenImgDN=len(sMp3DN)
            oLog.logDbg('execMain:sMp3DN:%r iLenMp3DN:%d',sMp3DN,iLenImgDN)
            # ----- end:prepare batch processing
            # +++++ beg:walk through directories
            for sRoot,lDN,lFN in os.walk(sMp3DN):
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
                            sTrkFN=os.path.join(sRoot,sFN)
                            sOutFN=os.path.join(sOutDN,sRelDN,sFN[:iPosExt])
                            oLog.logDbg('    sOutDN:%r sRelDN:%r',sOutDN,sRelDN)
                            oLog.logDbg('    sTmpFN:%r sOutFN:%r',sTmpFN,sOutFN)
                            # ----- end:generate output filename
                            # +++++ beg:perform ocr
                            iR=updMp3Tag(sTmpFN,
                                    sTrkFN=sTrkFN,
                                    sOutFN=sOutFN,
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
    oArg.addOpt('sMp3DN',
            sDft='./mp3',
            sHlp='audio folder',
            sMeta='./folder/to/visit')
    oArg.addOpt('sTrkDN',
            sDft=None,
            sHlp='track folder',
            sMeta='./floder/to/visit')
    oArg.addOpt('sKind',
            sDft='str',
            sHlp='conversion output format',
            sMeta='str|xml|str|xmlRaw')
    oArg.addOpt('iShow',
            sDft=0,
            sHlp='show images',
            sMeta='0|1')
    
    oArg.addOpt('sLogFN',
            sDft='./log/bthvn10.log',
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
                sTrkDN          =getattr(oArg,"sTrkDN"),
                sMp3DN          =getattr(oArg,"sMp3DN"),
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
