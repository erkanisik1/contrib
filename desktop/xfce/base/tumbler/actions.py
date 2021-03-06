#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	autotools.configure("--prefix=/usr \
	--enable-gstreamer-thumbnailer \
	--enable-poppler-thumbnailer \
	--enable-desktop-thumbnailer \
	--enable-pixbuf-thumbnailer \
	--enable-cover-thumbnailer \
	--enable-font-thumbnailer \
	--enable-jpeg-thumbnailer \
	--enable-odf-thumbnailer \
	--enable-xdg-cache \
	\
	--disable-ffmpeg-thumbnailer \
	--disable-raw-thumbnailer \
	--disable-static")

	pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("README", "NEWS", "COPYING", "ChangeLog", "AUTHORS")
