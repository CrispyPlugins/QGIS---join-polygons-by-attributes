# -*- coding: utf-8 -*-
"""
/***************************************************************************
 JoinByAttribute
                                 A QGIS plugin
 This plugin joins polygons with the same attribute.
                             -------------------
        begin                : 2017-02-08
        copyright            : (C) 2017 by crispy Plugins
        email                : crispy.plugins@t-online.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load JoinByAttribute class from file JoinByAttribute.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .join_by_attribute import JoinByAttribute
    return JoinByAttribute(iface)
