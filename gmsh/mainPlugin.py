# author  : Jonathan Lambrechts jonathan.lambrechts@uclouvain.be
# licence : GPLv2 (see LICENSE.md)

from . import exportGeometry
from . import runGmsh
from . import loadMsh

class GmshPlugin:

    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.loadMshAction = loadMsh.createAction(self.iface)
        self.meshAction = runGmsh.createAction(self.iface, self.loadMshAction.dialog)
        self.geoAction = exportGeometry.createAction(self.iface, self.meshAction.dialog)
        self.iface.addPluginToMenu("&Gmsh", self.geoAction)
        self.iface.addPluginToMenu("&Gmsh", self.meshAction)
        self.iface.addPluginToMenu("&Gmsh", self.loadMshAction)

    def unload(self):
        pass
        self.iface.removePluginMenu("&Gmsh", self.geoAction)
        self.iface.removePluginMenu("&Gmsh", self.meshAction)
        self.iface.removePluginMenu("&Gmsh", self.loadMshAction)

