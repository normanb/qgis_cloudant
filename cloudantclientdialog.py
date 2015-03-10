"""
/***************************************************************************
 CloudantClientDialog
                                 A QGIS plugin
 Cloudant Client
                             -------------------
        begin                : 2014-12-01
        copyright            : (C) 2014 by Norman Barker
        email                : norman@cloudant.com
        website              : https://www.cloudant.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_cloudantclient import Ui_CloudantClient
from qgis.core import *
from osgeo import gdal

import string
import random
import tempfile
import os
import os.path
import re

plugin_path = os.path.abspath(os.path.dirname(__file__))

class CloudantClientDialog(QtGui.QDialog):

	def __init__(self, parent):
		QtGui.QDialog.__init__(self)
		# Set up the user interface from Designer.
		self.parent = parent
		self.ui = Ui_CloudantClient()
		self.ui.setupUi(self)

		self.ui.lblWarning.setVisible(False)

		# Load default cloudant url
		self.ui.txtUrl.setText(self.get_url())

		self.ui.txtUsername.setReadOnly(True)
		self.ui.txtPassword.setReadOnly(True)

		self.parameter_lineedits = []
		self.parameter_labels = []

		self.settings = QtCore.QSettings()
		self.init_variables()

		QtCore.QObject.connect(self.ui.cmdSaveUrl, QtCore.SIGNAL("clicked()"), self.save_url)
		QtCore.QObject.connect(self.ui.txtUrl, QtCore.SIGNAL("textChanged(QString)"), self.check_url)
		QtCore.QObject.connect(self.ui.chkAuthentication, QtCore.SIGNAL("clicked()"), self.update_authentication)
		QtCore.QObject.connect(self.ui.cmdGetFeature, QtCore.SIGNAL("clicked()"), self.getFeature)

		self.check_url(self.ui.txtUrl.text().strip())

		# configure proxy settings
		self.configure_proxy()

	def init_variables(self):
		self.bbox = ""

	def configure_proxy(self):
		proxyEnabled = self.settings.value("proxy/proxyEnabled", "")
		proxyHost = self.settings.value("proxy/proxyHost", "")
		proxyPort = self.settings.value("proxy/proxyPort", "")
		proxyUser = self.settings.value("proxy/proxyUser", "")
		proxyPassword = self.settings.value("proxy/proxyPassword", "")
		
		if proxyEnabled:
			#host
			if proxyHost is not None and proxyPort is not None:
				gdal.SetConfigOption('GDAL_HTTP_PROXY', str(proxyHost) + ':' + str(proxyPort))
			elif proxyHost is not None:
				gdal.SetConfigOption('GDAL_HTTP_PROXY', proxyHost)
			#user
			if proxyUser is None and proxyPassword is None:
				gdal.SetConfigOption('GDAL_HTTP_PROXYUSERPWD', '%s:%s' % (proxyUser, proxyPassword))

	# Process GetFeature
	def getFeature(self):
		# get dbname and create layer
		url = self.ui.txtUrl.text().strip()
		self.lock_ui()
		self.create_layer(url)
		self.unlock_ui()
		self.close()

	"""
	############################################################################################################################
	# UI
	############################################################################################################################
	"""


	# UI: url warning
	def check_url(self, url):
		pass

	# UI: Update Main-Frame / Enable|Disable Authentication
	def update_authentication(self):
		if not self.ui.chkAuthentication.isChecked():
			self.ui.txtUsername.setReadOnly(True)
			self.ui.txtPassword.setReadOnly(True)
			self.ui.txtUsername.clear()
			self.ui.txtPassword.clear()
		else:
			self.ui.txtUsername.setReadOnly(False)
			self.ui.txtPassword.setReadOnly(False)

	def lock_ui(self):
		self.ui.cmdGetFeature.setEnabled(False)
		self.ui.cmdSaveUrl.setEnabled(False)

	def unlock_ui(self):
		self.ui.cmdGetFeature.setEnabled(True)
		self.ui.cmdSaveUrl.setEnabled(True)

	def create_layer(self, url):
		dbname = url.split("/")[-1]
		if (dbname == "_all_docs"):
			dbname = url.split("/")[-2]

		if self.ui.chkAuthentication.isChecked():
			usr = self.ui.txtUsername.text().strip()
			pswd = self.ui.txtPassword.text().strip()
			# split on either http:// or https://
			if len(usr) > 0 and len(pswd) > 0:
				if url.startswith('http://'):
					url = 'http://%s:%s@%s' % (usr, pswd, url[7:])
				elif url.startswith('https://'):
					url = 'https://%s:%s@%s' % (usr, pswd, url[8:])

		vlayer = QgsVectorLayer("cloudant:" + url, dbname, "ogr")
		if not vlayer.isValid():
			QtGui.QMessageBox.critical(self, "Error", "Response is not a valid QGIS-Layer!")
			self.ui.lblWarning.setText("<span style=\"color:red\">Response is not a valid QGIS-Layer!</span>")
			self.ui.lblWarning.setVisible(True)
		else:
			self.ui.lblWarning.setVisible(False)
			self.ui.lblWarning.setText("")
			# QGIS 1.8, 1.9
			if hasattr(QgsMapLayerRegistry.instance(), "addMapLayers"):
				QgsMapLayerRegistry.instance().addMapLayers([vlayer])
			# QGIS 1.7
			else:
				QgsMapLayerRegistry.instance().addMapLayer(vlayer)
			
			self.parent.iface.mapCanvas().refresh()
			self.parent.iface.zoomToActiveLayer()

	"""
	############################################################################################################################
	# UTIL
	############################################################################################################################
	"""

	def logMessage(self, message):
		if globals().has_key('QgsMessageLog'):
			QgsMessageLog.logMessage(message, "CloudantClient")

	def save_url(self):
		self.save_tempfile("cloudantclient.txt", str(self.ui.txtUrl.text().strip()))
		QtGui.QMessageBox.information(self.parent.iface.mainWindow(),"Info", "Successfully saved url!" )

	def get_url(self):
		try:
			tmpdir = os.path.join(tempfile.gettempdir(),'cloudantclient')
			tmpfile= os.path.join(tmpdir, "cloudantclient.txt")
			fobj=open(tmpfile,'r')
			url = fobj.readline()
			fobj.close()
			return url
		except IOError, e:
			return "https://geodemo001.cloudant.com/gdaltest"

	def get_temppath(self, filename):
		tmpdir = os.path.join(tempfile.gettempdir(),'cloudantclient')
		if not os.path.exists(tmpdir):
			os.makedirs(tmpdir)
		tmpfile= os.path.join(tmpdir, filename)
		return tmpfile

	def save_tempfile(self, filename, content):
		tmpdir = os.path.join(tempfile.gettempdir(),'cloudantclient')
		if not os.path.exists(tmpdir):
			os.makedirs(tmpdir)
		tmpfile= os.path.join(tmpdir, filename)
		fobj=open(tmpfile,'wb')
		fobj.write(content)
		fobj.close()
		return tmpfile
