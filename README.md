# FACEPASS

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

Facepass is a system which carries out real-time facial detection, recognition and subsequently identifies the individual along with their information. Initally developed within the context of a University where the system is able to facilitate access to multiple areas including but not limited to the campus premises, classrooms and examination rooms.

This system is based on the open-source computer vision (OpenCV) library, Python, MySQL
and Django web framework. 

The system provides functionality and capability of recognizing a face, adding
it to the dataset and identifying the face linked with a record in the database with acceptable
performance. 



  - Incorporate computer vision techniques to obtain images
from live video input and subsequently detect facial features.
  - Able to capture biometric information and admission
numbers from students
  - Identify who the face belongs to and display all the
relevant information stored in the database pertaining to them.
  




### Languages & Libraries



* Python 
* Django 
* OpenCV 
* Scikit-learn
* Mysql




### Installation

This system is built up Django a Python web framework, thus requiring Python to be installed on your machine.

To install Python on your machine go to https://python.org/download/, and download a Windows MSI installer for Python. Once downloaded, run the MSI installer and follow the on-screen instructions.

After installation, open the command prompt and check the Python version by executing python --version. If you encounter a problem, make sure you have set the PATH variable correctly. You might need to adjust your PATH environment variable to include paths to the Python executable and additional scripts. For example, if your Python is installed in C:\Python34\, the following  needs to be added to PATH:

```sh
C:\Python34\;C:\Python34\Scripts;
```

PIP is a package manager for Python that you will use  to install Django, OpenCV and other libraries from PyPI. If you have installed Python 3.4 pip is already included. http://www.pip-installer.org/en/latest/installing.html for installation instructions.

Once PIP is installed execute the following in the command prompt to download and install Django: 

```sh
pip install django
```

Execute the following in the command prompt to download and install OpenCV:
```sh
pip install opencv-python
```
Execute the following in the command prompt to download and install the other libraries:
```sh
pip install numpy
pip install scipy
pip install scikit-learn
```


This system employs the use of MySQL. One can host the database with the aid of 

**Xampp** https://www.apachefriends.org/download.html

**MySQL Workbench** https://dev.mysql.com/downloads/workbench/

