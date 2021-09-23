## fedora34

[fedora](https://fedoramagazine.org/things-to-do-after-installing-fedora-34-workstation/)

```shell
sudo dnf group upgrade --with-optional Multimedia
```

```shell
sudo dnf install gnome-tweaks
sudo dnf install gnome-extensions-app
```

**vscode**

[vscode](https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions)

```shell
sudo dnf install code
sudo sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'
dnf check-update
sudo dnf install code
```

**OpenRefine**

[OpenRefine](https://openrefine.org/download.html)

**vls**

+ [vlc](dnf install python-vlc)

```shell
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install vlc
sudo dnf install python-vlc
```

**git**

[git](https://git-scm.com/)

```shell
sudo dnf install git-lfs
```

**wxPython**

[wxPython](https://wxpython.org/)

```shell
sudo dnf install python3-wxpython4-webview
```

**tesserAct**

[tesserAct](https://pypi.org/project/pytesseract/)

```shell
sudo dnf install tesseract
pip install pytesseract
```

**openCV**

[openCV](pip install opencv-python)

```shell
sudo pip install cv2
```

**VMware**

[VMwaare](https://www.tecmint.com/install-vmware-workstation-in-linux/)

```shell
wget https://download3.vmware.com/software/wkst/file/VMware-Workstation-Full-16.1.0-17198959.x86_64.bundle
chmod a+x VMware...
sudo yum groupinstall "Development tools"
sudo yum install kernel-headers	
sudo yum install kernel-devel 
```

**blender**

[blender](https://www.blender.org/)

```shell
sudo dnf install gcc gcc-c++ git subversion make cmake libX11-devel libXxf86vm-devel libXi-devel libXcursor-devel libXrandr-devel libXinerama-devel libstdc++-static
```

```shell
mkdir ~/blender-git
cd ~/blender-git
git clone https://git.blender.org/blender.git
```

[build](https://wiki.blender.org/wiki/Building_Blender/Linux/Fedora#Automatic_Dependency_Installation)

```shell
cd ~/blender-git
./blender/build_files/build_environment/install_deps.sh
```

cmake

```shell
mkdir ~/blender-git/build
cd ~/blender-git/build
cmake ../blender
```

make

```shell
cd ~/blender-git/build
make
make install
```

install

```shell
cd ~/blender-git/blender
make update
cd ~/blender-git/build
make
make install
```

**OBS Studio**

```shell
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
sudo dnf install obs-studio
```

remote desktop

```shell
sudo dnf install remmenia
```

**python**

```shell
pip install six
pip install lxml
pip install pyodbc
pip install mathlib
pip install matplotlib
pip install numpy
pip install scipy
pip install requests
pip install bs4
pip install selenium
pip install pytesseract
pip install wxPython
pip install xlrd
pip install openpyxl
pip install spacy
python -m spacy download en_core_web_sm
```

```shell
pip install cupy
```
