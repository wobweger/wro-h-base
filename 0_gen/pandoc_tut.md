## tutorial

### start windows shell
mount [wroPrg05D.vmdk](wroPrg05D_vmdk.md) on drive G:

start windows shell and configure environment.
```
G:/data/env/exc.bat py24C win 2_py24C
```

```
environment           py24C
setup base            environment
                      BaseDirEng      G:
                      BaseDirPrg      G:\prog
                      BaseDirBin      G:\data\bin
                      BaseDirVid      V:
                      BaseDirUtil     G:\util
                      VENG_DN         G:
                      VPRG_DN         G:\prog
                      VDAT_DN         G:\data
                      VBIN_DN         G:\data\bin
                      VTMP_DN         G:\tmp
setup source
                      VSRC_PY_DN      V:/python
find architecture
                      CPU src          wn10D
                      CPU dst          wn10D
setup emacs24v3       environment
      emacs           base            g:\prog\emacs-24v3
setup py24C           environment
setup py24C           path            G:\prog\python24
setup mgwC            environment
setup mgwC            path            G:\prog\MinGW32
setup CMake           environment
setup CMake           path            G:\prog\cmake-3.4.0-winC
setup NSIS            environment
setup NSIS            path            G:\prog\nsis2v46
setup swig3           environment
setup swig3           path            G:\prog\swigwin-3.0.7
setup jdk18           environment
setup jdk18           path            G:\prog/java/jdk1.8.0_60
setup ANT             environment
setup ANT             path            G:/prog/apache/ant_1.9.6/bin
setup perl            environment
                      perl            skipped
setup miktex          environment
                      VP_MIKTEX_DN    G:\prog\miktex\miktex\bin
setup
      VP_SYSTEM       win
      LOC_TARGET_DN
      EXEC_TARGET
setup win             environment
setup win             path            G:\prog\usr
setup doxygen         environment
                      DOXYGEN_DN      G:\prog\doxygen
setup graphviz        environment
                      GRAPHVIZ_DN     G:\prog\graphviz-2v38\release\bin
                      MSCGEN_DN       G:\prog\graphviz-2v38\mscgen-0v20\bin
setup pandoc          environment
                      PANDOC_DN       G:\prog\pandoc-2.5
setup msvsc           environment
                      MSVSC_DN        G:\apps\msvsc
The system cannot find the batch label specified - fin
start ...
The system cannot find the drive specified.
```

### create html

```
G:\data>cd /d E:\dat\prog_inst
```

```E:\dat\prog_inst>dir
 Volume in drive E is data
 Volume Serial Number is 0E79-1E5A

 Directory of E:\dat\prog_inst

2018-12-29  11:54    <DIR>          .
2018-12-29  11:54    <DIR>          ..
2018-12-29  11:52             2,325  index.html
2018-12-29  11:43    <DIR>          .vscode
2018-12-29  11:07    <DIR>          1_common
2018-12-22  10:26    <DIR>          2_net
2018-12-22  10:26    <DIR>          3_dbs
2018-12-22  10:26    <DIR>          4_py24
2018-12-22  10:26    <DIR>          4_py25
2018-12-22  10:26    <DIR>          4_py26
2018-12-22  10:26    <DIR>          4_py27
2018-12-22  10:27    <DIR>          4_py34
2018-12-22  10:28    <DIR>          4_pyScript
2018-12-22  10:28    <DIR>          5_java
2018-12-22  10:29    <DIR>          5_perl
2018-12-29  11:32    <DIR>          6_cpp
2018-12-29  11:32    <DIR>          7_add
2018-12-22  10:30    <DIR>          7_prg
2018-12-29  11:33    <DIR>          8_doc
2018-12-22  10:30    <DIR>          8_misc
2018-12-22  10:31    <DIR>          8_web
2018-12-22  10:31    <DIR>          9_cfg
2018-12-22  10:31    <DIR>          D_drv
2018-12-22  10:31    <DIR>          E_release
2013-06-02  20:02             2,133 icon.txt
2013-06-02  19:10           204,755 IconizerBin32.zip
2018-12-29  11:55             2,336 index.html
2013-06-02  19:11       204,373,616 open_icon_library-standard-0.11.tar.bz2
2013-06-02  19:16       206,847,725 open_icon_library-standard-0.11.tar.bz2_20130602_vmprog04.7z
2008-08-09  22:32             1,736 prog.lnk
2018-12-22  10:33    <DIR>          P_portable
2018-12-29  11:27             1,031 README.md
2018-12-27  07:37    <DIR>          R_apps
2013-07-19  15:03            57,048 sapnote_0001088980_SolMng_inst.pdf
2011-02-16  21:01        16,171,267 ssvnc-1.0.28.tar.gz
2016-02-26  07:09         3,182,256 TeamViewerQSvidarc_en.exe
2013-06-02  19:09         9,353,800 ToolbarIcons-full-20101107.tar.gz
2007-09-09  10:39               875 VidMod_16.gif
2008-08-10  19:09            13,996 vLauncher_prog.xml
2018-12-22  10:35    <DIR>          X_vidarc
2018-12-22  10:36    <DIR>          zyToSort
2018-12-22  10:38    <DIR>          Z_SysTools
              14 File(s)    440,214,899 bytes
              28 Dir(s)  172,586,752,000 bytes free
```

```
E:\dat\prog_inst>pandoc -f markdown -o index.html README.md 1_common/README.md
```

```
E:\dat\prog_inst>pandoc -f markdown -o index.html README.md .\1_common\README.md
```


```
E:\dat\prog_inst>pandoc -f markdown -t html -o index.html .\1_common\README.md
```

```
E:\dat\prog_inst>pandoc -f markdown -o index.pdf README.md  ./1_common/README.md
Qt: Untested Windows version 10.0 detected!
Qt: Untested Windows version 10.0 detected!
```

### convert pdf to markdown

start windows shell
G:\>q:

Q:\>cd Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual

Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>pandoc PID_enUS_en-US_201703.pdf -o PID.md
Unknown reader: pdf
Pandoc can convert to PDF, but not from PDF.

Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>pandoc -f pdf PID_enUS_en-US_201703.pdf -o PID.md
Unknown reader: pdf
Pandoc can convert to PDF, but not from PDF.

Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>pandoc -f pdf PID_enUS_en-US_201703.docx -o PID.md
Unknown reader: pdf
Pandoc can convert to PDF, but not from PDF.

Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>pandoc  PID_enUS_en-US_201703.docx -o PID.md

Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>pandoc  pdf PID_enUS_en-US_201703.docx -o PID_01.md
pandoc: pdf: openBinaryFile: does not exist (No such file or directory)

Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>pandoc  109480739_COMOS_PID_best_practice_document_en.docx -o pract_doc.md
pandoc: Out of memory


Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>pandoc  109480739_COMOS_PID_best_practice_document_en.odt -o pract_odt.md
pandoc: Out of memory


Q:\csc\wro-h-howto\A_cos\M22_PnID\m_manual>

