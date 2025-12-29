#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    # Install the shell script to /usr/local/bin and rename it to remove .sh extension
    pisitools.insinto("/usr/local/bin", "files/kde-menu-watcher.sh", "kde-menu-watcher")
    
    # Install the autostart desktop file
    pisitools.insinto("/etc/xdg/autostart", "files/kde-menu-watcher.desktop")
    
    # Ensure the script is executable (pisitools should handle this but explicit is good)
    pisitools.chmod("/usr/local/bin/kde-menu-watcher", 0o755)
