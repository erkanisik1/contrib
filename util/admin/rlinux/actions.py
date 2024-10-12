#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt
from pisi.actionsapi import get, pisitools, shelltools


def setup():
    shelltools.system("pwd")
    shelltools.system("ar xf RLinux6_x64.deb")
    shelltools.system("tar xf data.tar.gz")


def install():
     pisitools.insinto("/", "usr")

