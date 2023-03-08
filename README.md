# swapsys - a linux cmd line utility program to manage swap space
A Python package to add swap space to a Linux system

![GitHub language count](https://img.shields.io/github/languages/count/rbashish/add-swap-space?style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/add-swap-space?style=plastic)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/add-swap-space?style=plastic)



![GitHub issues](https://img.shields.io/github/issues/rbashish/add-swap-space?style=plastic)
![PyPI - License](https://img.shields.io/pypi/l/add-swap-space?style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dm/add-swap-space?color=orange&label=PyPI%20downloads&style=plastic)


Description
-----
This package provides a command-line interface to add swap space to a Linux system.

It prompts the user for the desired swap size in GB and then adds the swap space using the dd and mkswap commands. After the swap space has been added, it updates `/etc/fstab` to make the swap permanent.

Download & Install
-----
```
pip install swapsys
```

`Note:` If pip is unrecognized try pip3 instead. 

Usage
----
```
sudo python3 -m swapsys
```
`Note:` Make sure you have pip install under root user as updating /etc/fstab requires root permission.

Screenshot
----
![pypi-add-swap-space.png](https://github.com/rbashish/add-swap-space/blob/main/image/pypi-add-swap-space.png)

Feedback/Issue
----
Have a feedback, feature request, known bug, please report it at this [issue page](https://github.com/rbashish/swapsys/issues)
