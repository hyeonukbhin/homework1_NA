# homework1_NA
homework1 on Numerical Analysis using PyThon

Install PyQt5, QtSql and Qt5 designer for Python3 on Ubuntu
Sorry, I meant "I'm gonna open the terminal" not interpreter. 

sudo apt-get install python3-pyqt5
sudo apt-get install python3-pyqt5.qtsql
sudo apt-get install qttools5-dev-tools

**** Desktop Launcher***
[Desktop Entry]
Name=Qt5 Designer
Icon=/home/mserag/Pictures/icons/qt5-designer.png
Exec=/usr/lib/x86_64-linux-gnu/qt5/bin/designer
Type=Application
Categories=Application
Terminal=false
StartupNotify=true
Actions=NewWindow

Name[en_US]=Qt5 Designer

[Desktop Action NewWindow]
Name=Open a New Window
Exec=/usr/lib/x86_64-linux-gnu/qt5/bin/designer

********************************************
add that code to a file, name it anything but with extension '.desktop' and stick it in ~/.local/share/applications/