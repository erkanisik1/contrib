#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools, shelltools, get

WorkDir = "."
NoStrip = ["/"]



def install():
    # Antigravity IDE dosyalarını /opt altına kopyala
    pisitools.insinto("/opt/Antigravity-ide", "Antigravity IDE/*")

    # completions dizinini kaldır (pspec.xml'deki AdditionalFiles ile yönetiliyor)
    #pisitools.removeDir("/opt/Antigravity-ide/resources/completions")

    # Çalıştırılabilir dosya için symlink oluştur
    #pisitools.dosym("/opt/Antigravity-ide/antigravity-ide", "/usr/bin/antigravity-ide")

    # Lisans dosyaları için symlink oluştur
    pisitools.dodir("/usr/share/licenses/Antigravity-ide")
    pisitools.dosym("/opt/Antigravity-ide/resources/app/LICENSE.txt", "/usr/share/licenses/Antigravity-ide/LICENSE.txt")
    pisitools.dosym("/opt/Antigravity-ide/LICENSES.chromium.html", "/usr/share/licenses/Antigravity-ide/LICENSES.chromium.html")