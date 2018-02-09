# resourceMonitor/installTasks.py
# Copyright 2017 Joseph Lee, released under GPL.

# Provides needed routines during add-on installation and removal.
# Mostly checks compatibility.
# Routines are partly based on other add-ons, particularly Place Markers by Noelia Martinez (thanks add-on authors).

import sys
import gui
import wx
import addonHandler
addonHandler.initTranslation()

def onInstall():
	requiredVer = "Windows 7 Service Pack 1, Windows Server 2008 R2 Service Pack 1"
	# Translators: Dialog text shown when attempting to install the add-on on an unsupported version of Windows (minSupportedVersion is the minimum version required for this add-on).
	if sys.getwindowsversion().build < 7601 and gui.messageBox(_("Support for Windows Vista, Server 2003 and 2008 from Resource Monitor add-on is ending on June 2018. Future add-on releases will require {minSupportedVersion} or later. Are you sure you wish to install this add-on anyway?").format(minSupportedVersion = requiredVer),
	# Translators: title of the dialog shown when attempting to install the add-on on an old version of Windows.
	_("Old Windows version"), wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.NO:
		raise RuntimeError("Old Windows version detected")
