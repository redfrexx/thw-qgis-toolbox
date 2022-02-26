# -*- coding: utf-8 -*-

"""
/***************************************************************************
 THW
                                 A QGIS plugin
 Tools for supporting THW 
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-02-19
        copyright            : (C) 2022 by Christina Ludwig (THW Heidelberg)
        email                : christina.ludwig@thw-heidelberg.de
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

__author__ = 'Christina Ludwig (THW Heidelberg)'
__date__ = '2022-02-19'
__copyright__ = '(C) 2022 by Christina Ludwig (THW Heidelberg)'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os
import sys
import inspect

from qgis.core import QgsProcessingAlgorithm, QgsApplication
from .thw_provider import THWProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class THWPlugin(object):

    def __init__(self):
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = THWProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)