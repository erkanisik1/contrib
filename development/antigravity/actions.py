#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/"]



def install():
    pisitools.insinto("/opt/Antigravity", "Antigravity-x64/*")
    pisitools.dosym("/opt/antigravity/antigravity", "/usr/bin/antigravity")
    pisitools.dosym("/opt/Antigravity/LICENSE.electron.txt", "/usr/share/licenses/antigravity/LICENSE.electron.txt")
    pisitools.dosym("/opt/Antigravity/LICENSES.chromium.html", "/usr/share/licenses/antigravity/LICENSES.chromium.html")
    pisitools.dosym("/opt/Antigravity/LICENSE", "/usr/share/licenses/antigravity/LICENSE")