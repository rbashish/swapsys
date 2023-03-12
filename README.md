# swapsys - a linux cmd line utility to manage swap space

![PyPI Version](https://img.shields.io/pypi/v/swapsys?style=plastic)
![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/swapsys?style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/swapsys?style=plastic)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/swapsys?style=plastic)

![GitHub issues](https://img.shields.io/github/issues-raw/rbashish/swapsys?style=plastic)
![PyPI - License](https://img.shields.io/pypi/l/swapsys?style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dm/swapsys?style=plastic)


Description
-----
This package provides a command-line interface to manage swap space to a Linux system.

It prompts the user for the desired swap size in GB and then adds the swap space using the dd and mkswap commands. After the swap space has been added, it updates `/etc/fstab` to make the swap permanent.
It also has an options of removing, increasing and decreasing the memory size.

Download & Install
-----
```
pip install swapsys
```

`Note:` Please note that some operating systems might be equipped with the python3 and pip3 commands instead of python and pip. 

Usage
----
```
swapsys
```
`Note:` Make sure you provide full path of swapsys (`which swapsys` to get the path) with sudo or run with root user as updating /etc/fstab requires root permission.

Screenshot
----
### Downloading the package:
![pypi-swapsys.png](https://raw.githubusercontent.com/rbashish/swapsys/main/image/pip-install-swapsys.png)

### Run the utility 
![pypi-swapsys.png](https://raw.githubusercontent.com/rbashish/swapsys/main/image/swapsys-logo.png)

Feedback/Issue
----
Have a feedback, feature request, known bug, please report it at this [issue page](https://github.com/rbashish/swapsys/issues)
