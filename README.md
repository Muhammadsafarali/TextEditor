# TextEditor

## Описание

Программа умеет:

  * открывать файл;
  * сохранять файл;
  * закрываться;
  * читать и записывать в юникоде.
  
Программа написана с использованием:

  * PyQt4;
  * Qt Designer;
  * Pycharm.

## Источник вдохновения:

1) [rkblog.rk.edu.pl][id];

[id]:http://www.rkblog.rk.edu.pl/w/p/simple-text-editor-pyqt4/


<img src="https://github.com/Muhammadsafarali/TextEditor/blob/master/TextEditor.png" width="500">


###Установка PyQt4

```bash
  sudo apt-get install python-qt4
```

```python
import sys
from PyQt4.QtGui import *
app = QApplication(sys.argv)
button = QPushButton("Hello World", None)
button.show()
app.exec_()
```

Для удобной трансляции ui-файлов «дизайнера» в Python-код была использована программа pyuic4 
--- 
из пакета-посредника между Qt Designer и Python, которая называется pyqt4-dev-tools.

###Установка **`pyqt4-dev-tools`**:

```bash
  sudo apt install pyqt4-dev-tools
```  
  
###Использование:

```bash
  pyuic4 designer.ui > designer.py
```  
  
  ***
###Полезные ссылки:

1) [хабр про PyQt4][id1];
2) [how to install PyQt4][id2];




[id1]:https://habrahabr.ru/post/75226/
[id2]:http://www.saltycrane.com/blog/2008/01/how-to-install-pyqt4-on-ubuntu-linux/
