"""
/***************************************************************************
 CloudantClient
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from cloudantclientdialog import CloudantClientDialog

class CloudantClient:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/cloudantclient/icon.png"), \
            "Client", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        self.aboutAction=QAction(QIcon(":/plugins/cloudantclient/icon.png"), \
            "About", self.iface.mainWindow())
        QObject.connect(self.aboutAction, SIGNAL("activated()"), self.about)

        # Add toolbar button and menu item
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.addPluginToWebMenu("&Cloudant", self.action)
            self.iface.addPluginToWebMenu("&Cloudant", self.aboutAction)
            self.iface.addWebToolBarIcon(self.action)
        else:
            self.iface.addToolBarIcon(self.action)
            self.iface.addPluginToMenu("&Cloudant", self.action)
            self.iface.addPluginToMenu("&Cloudant", self.aboutAction)

    def unload(self):
        # Remove the plugin menu item and icon
        if hasattr( self.iface, "addPluginToWebMenu" ):
            self.iface.removePluginWebMenu("&Cloudant", self.action)
            self.iface.removePluginWebMenu("&Cloudant", self.aboutAction)
            self.iface.removeWebToolBarIcon(self.action)
        else:
            self.iface.removeToolBarIcon(self.action)
            self.iface.removePluginMenu("&Cloudant", self.action)
            self.iface.removePluginMenu("&Cloudant", self.aboutAction)

    def about(self):
        infoString = "<table><tr><td colspan=\"2\"><b>Cloudant Client 0.0.1</b></td></tr><tr><td colspan=\"2\"></td></tr><tr><td>Author:</td><td>Norman Barker</td></tr><tr><td>Mail:</td><td><a href=\"mailto:norman@cloudant.com\">norman@cloudant.com</a></td></tr><tr><td>Website:</td><td><a href=\"https://www.cloudant.com\">https://www.cloudant.com</a></td></tr></table>"
        QMessageBox.information(self.iface.mainWindow(), "About Cloudant Client", infoString)

    # run method that performs all the real work
    def run(self):

        # create and show the dialog
        dlg = CloudantClientDialog(self)
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass
