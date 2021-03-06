#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--enable-jit \
                         --enable-pcre2test-libreadline \
                         --enable-pcre2-32 \
                         --enable-pcre2-16 \
                         --enable-unicode \
                         --docdir=/%s/%s \
                         --disable-static" % (get.docDIR(), get.srcNAME()))
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def check():
    if get.buildTYPE() == "emul32":
        pass
    else:
        autotools.make("-j1 check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
